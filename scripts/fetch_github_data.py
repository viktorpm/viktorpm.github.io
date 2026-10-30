#!/usr/bin/env python3
"""
GitHub Data Fetcher for viktorpm.github.io

This script fetches user profile, organization, and repository data from GitHub
using the GraphQL API. It generates JSON data files used by the Jekyll site to
display dynamic content.

Requirements:
- GitHub Personal Access Token with scopes: read:user, read:org, repo
- Python 3.6+

Usage:
    python3 scripts/fetch_github_data.py

The script will prompt for the GitHub token interactively for security.
"""

import getpass
import json
import os
import sys
import urllib.error
import urllib.request

GQL_ENDPOINT = "https://api.github.com/graphql"


# Authentication and API access
def get_credentials():
    """Read GitHub credentials from the environment or prompt locally."""
    user_login = os.environ.get("GH_USER", "viktorpm")
    token = os.environ.get("GH_TOKEN")

    if not token:
        print("Please enter your GitHub personal access token.")
        print("Required permissions: read:user, read:org")
        token = getpass.getpass("GitHub Token: ").strip()
        if not token:
            print("No token provided. Exiting.", file=sys.stderr)
            sys.exit(1)
    else:
        print("Using GitHub token from environment (CI mode)")

    if (
        not os.environ.get("GH_TOKEN")
        and user_login == "viktorpm"
        and not os.environ.get("GH_USER")
    ):
        username_input = input("GitHub username (default: viktorpm): ").strip()
        if username_input:
            user_login = username_input

    return token, user_login


def gql(query, token, variables=None):
    data = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
    req = urllib.request.Request(GQL_ENDPOINT, data=data, method="POST")
    req.add_header("Authorization", f"bearer {token}")
    req.add_header("Content-Type", "application/json")
    
    try:
        with urllib.request.urlopen(req) as resp:
            response_body = resp.read().decode("utf-8")
            out = json.loads(response_body)
            
        if "errors" in out:
            print(f"GraphQL errors: {out['errors']}", file=sys.stderr)
            raise RuntimeError(out["errors"])
            
        if "data" not in out:
            print(f"Unexpected response format: {out}", file=sys.stderr)
            raise RuntimeError("No 'data' field in response")
            
        return out["data"]
        
    except urllib.error.HTTPError as e:
        error_body = ""
        try:
            error_body = e.read().decode("utf-8")
        except OSError:
            error_body = "Could not read error details"
            
        if e.code == 401:
            print(f"Authentication failed (401 Unauthorized)", file=sys.stderr)
            print(f"Please check your GitHub token. Make sure it has the required permissions:", file=sys.stderr)
            print(f"- read:user", file=sys.stderr)
            print(f"- read:org", file=sys.stderr)
            if error_body:
                print(f"Error details: {error_body}", file=sys.stderr)
            print(f"Token starts with: {token[:8]}..." if len(token) > 8 else f"Token length: {len(token)} chars", file=sys.stderr)
        else:
            print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)
            if error_body:
                print(f"Error details: {error_body}", file=sys.stderr)
        raise

# GraphQL queries
PROFILE_MINIMAL_Q = """
query($login:String!) {
  user(login:$login) {
    name
    login
    bio
    company
    location
    websiteUrl
    avatarUrl
    url
  }
}
"""

# Pinned repositories query (should work with repo scope)
PINNED_REPOS_Q = """
query($login:String!) {
  user(login:$login) {
    pinnedItems(first: 6, types: REPOSITORY) {
      nodes {
        ... on Repository {
          name description url stargazerCount
          primaryLanguage { name }
          repositoryTopics(first: 8) { nodes { topic { name } } }
        }
      }
    }
  }
}
"""

# Organization query (requires read:org scope)
ORGS_Q = """
query($login:String!) {
  user(login:$login) {
    organizations(first: 50) {
      nodes { name login description url avatarUrl isVerified }
    }
  }
}
"""

RECENT_REPOS_Q = """
query($login:String!) {
  user(login:$login) {
    repositories(first: 30, privacy: PUBLIC, ownerAffiliations: OWNER,
      orderBy: {field: UPDATED_AT, direction: DESC}) {
      nodes {
        name description url stargazerCount forkCount updatedAt
        primaryLanguage { name }
        repositoryTopics(first: 8) { nodes { topic { name } } }
      }
    }
  }
}
"""


def flatten_topics(rt_nodes):
    return [n["topic"]["name"] for n in rt_nodes] if rt_nodes else []


def format_repo(repo, include_activity=False):
    """Convert a repository response to the site's JSON shape."""
    formatted = {
        "name": repo["name"],
        "description": repo.get("description"),
        "url": repo["url"],
        "stargazerCount": repo["stargazerCount"],
    }
    if include_activity:
        formatted.update({
            "forkCount": repo["forkCount"],
            "updatedAt": repo["updatedAt"],
        })
    formatted["primaryLanguage"] = repo.get("primaryLanguage")
    formatted["topics"] = flatten_topics(
        (repo.get("repositoryTopics") or {}).get("nodes", [])
    )
    return formatted


# Site-specific entries and role labels not provided by the API.
SUPPLEMENTAL_ORGS = [
    {
        "name": "No Black Boxes",
        "login": "NoBlackBoxes",
        "description": "Everyone can understand their tools.",
        "url": "https://github.com/NoBlackBoxes",
        "avatarUrl": "https://avatars.githubusercontent.com/u/86297273?v=4",
        "isVerified": False,
    },
]

ORG_ROLES = {
    "LIMLabSWC": "Admin & maintainer",
    "NoBlackBoxes": "Developer & teacher",
}

SUPPLEMENTAL_PINNED = [
    {
        "name": "LastBlackBox",
        "description": "A course for brains interested in brains (not tools interested in tools)",
        "url": "https://github.com/NoBlackBoxes/LastBlackBox",
        "stargazerCount": 65,
        "primaryLanguage": {"name": "Jupyter Notebook"},
        "topics": [],
    },
]


def merge_by_login(existing, supplemental):
    known = {item.get("login") for item in existing}
    merged = list(existing)
    for item in supplemental:
        if item.get("login") not in known:
            merged.append(item)
    return merged

def merge_pinned(existing, supplemental):
    known = {item.get("url") for item in existing}
    merged = [item for item in supplemental if item.get("url") not in known]
    merged.extend(existing)
    return merged


def apply_org_roles(orgs):
    for org in orgs:
        role = ORG_ROLES.get(org.get("login"))
        if role:
            org["role"] = role
    return orgs


# Fetch API data and write the files consumed by Jekyll
def main():
    token, user_login = get_credentials()
    os.makedirs("_data", exist_ok=True)
    
    # Get basic profile info
    try:
        d1 = gql(PROFILE_MINIMAL_Q, token, {"login": user_login})
        user = d1["user"]
        profile = {
            "name": user.get("name"),
            "login": user["login"],
            "bio": user.get("bio"),
            "company": user.get("company"),
            "location": user.get("location"),
            "websiteUrl": user.get("websiteUrl"),
            "avatarUrl": user.get("avatarUrl"),
            "url": user.get("url"),
        }
    except RuntimeError as e:
        error_str = str(e)
        if "INSUFFICIENT_SCOPES" in error_str:
            print("Warning: Cannot fetch profile data - token may need 'read:user' scope", file=sys.stderr)
            print("Using minimal profile data...", file=sys.stderr)
            profile = {
                "name": None,
                "login": user_login,
                "bio": None,
                "company": None,
                "location": None,
                "websiteUrl": None,
                "avatarUrl": None,
                "url": f"https://github.com/{user_login}",
            }
        else:
            raise

    # Get pinned repositories
    pinned = []
    try:
        pinned_data = gql(PINNED_REPOS_Q, token, {"login": user_login})
        for n in pinned_data["user"].get("pinnedItems", {}).get("nodes", []):
            pinned.append(format_repo(n))
    except RuntimeError as e:
        error_str = str(e)
        if "INSUFFICIENT_SCOPES" in error_str:
            print("Warning: Cannot fetch pinned repositories - continuing without them", file=sys.stderr)
        else:
            raise

    # Try to get organizations (requires read:org scope)
    orgs = []
    try:
        org_data = gql(ORGS_Q, token, {"login": user_login})
        for o in org_data["user"].get("organizations", {}).get("nodes", []):
            orgs.append({
                "name": o.get("name") or o["login"],
                "login": o["login"],
                "description": o.get("description"),
                "url": o["url"],
                "avatarUrl": o.get("avatarUrl"),
                "isVerified": o.get("isVerified"),
            })
    except RuntimeError as e:
        error_str = str(e)
        if "INSUFFICIENT_SCOPES" in error_str or "read:org" in error_str:
            print("Warning: Cannot fetch organization data - token needs 'read:org' scope", file=sys.stderr)
            print("Continuing without organization data...", file=sys.stderr)
        else:
            raise

    # Get recent repositories
    recent = []
    try:
        d2 = gql(RECENT_REPOS_Q, token, {"login": user_login})
        for r in d2["user"]["repositories"]["nodes"]:
            recent.append(format_repo(r, include_activity=True))
    except RuntimeError as e:
        error_str = str(e)
        if "INSUFFICIENT_SCOPES" in error_str:
            print("Warning: Cannot fetch recent repositories - token may need 'repo' scope", file=sys.stderr)
        else:
            raise

    orgs = apply_org_roles(merge_by_login(orgs, SUPPLEMENTAL_ORGS))
    pinned = merge_pinned(pinned, SUPPLEMENTAL_PINNED)

    with open("_data/github_profile.json", "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)
    with open("_data/orgs.json", "w", encoding="utf-8") as f:
        json.dump(orgs, f, ensure_ascii=False, indent=2)
    with open("_data/repos.json", "w", encoding="utf-8") as f:
        json.dump({"pinned": pinned, "recent": recent}, f, ensure_ascii=False, indent=2)

    print("Wrote _data/github_profile.json, _data/orgs.json, _data/repos.json")

if __name__ == "__main__":
    main()
