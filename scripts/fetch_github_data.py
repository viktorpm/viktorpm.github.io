import json, os, sys, datetime, textwrap
import urllib.request
import urllib.error
import getpass

GQL_ENDPOINT = "https://api.github.com/graphql"
USER_LOGIN = os.environ.get("GH_USER", "viktorpm")

# Always prompt for token interactively (ignore environment variable)
print("Please enter your GitHub personal access token.")
print("Required permissions: read:user, read:org")
TOKEN = getpass.getpass("GitHub Token: ").strip()
if not TOKEN:
    print("No token provided. Exiting.", file=sys.stderr)
    sys.exit(1)

# Allow interactive username input if using default
if USER_LOGIN == "viktorpm" and not os.environ.get("GH_USER"):
    username_input = input("GitHub username (default: viktorpm): ").strip()
    if username_input:
        USER_LOGIN = username_input

def gql(query, variables=None):
    data = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
    req = urllib.request.Request(GQL_ENDPOINT, data=data, method="POST")
    req.add_header("Authorization", f"bearer {TOKEN}")
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
        except:
            error_body = "Could not read error details"
            
        if e.code == 401:
            print(f"Authentication failed (401 Unauthorized)", file=sys.stderr)
            print(f"Please check your GitHub token. Make sure it has the required permissions:", file=sys.stderr)
            print(f"- read:user", file=sys.stderr)
            print(f"- read:org", file=sys.stderr)
            if error_body:
                print(f"Error details: {error_body}", file=sys.stderr)
            print(f"Token starts with: {TOKEN[:8]}..." if len(TOKEN) > 8 else f"Token length: {len(TOKEN)} chars", file=sys.stderr)
        else:
            print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)
            if error_body:
                print(f"Error details: {error_body}", file=sys.stderr)
        raise

# Minimal profile query that should work with repo scope
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

def main():
    os.makedirs("_data", exist_ok=True)
    
    # Get basic profile info
    try:
        d1 = gql(PROFILE_MINIMAL_Q, {"login": USER_LOGIN})
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
              "login": USER_LOGIN,
              "bio": None,
              "company": None,
              "location": None,
              "websiteUrl": None,
              "avatarUrl": None,
              "url": f"https://github.com/{USER_LOGIN}",
            }
        else:
            raise

    # Get pinned repositories
    pinned = []
    try:
        pinned_data = gql(PINNED_REPOS_Q, {"login": USER_LOGIN})
        for n in pinned_data["user"].get("pinnedItems", {}).get("nodes", []):
            pinned.append({
              "name": n["name"],
              "description": n.get("description"),
              "url": n["url"],
              "stargazerCount": n["stargazerCount"],
              "primaryLanguage": n.get("primaryLanguage"),
              "topics": flatten_topics((n.get("repositoryTopics") or {}).get("nodes", [])),
            })
    except RuntimeError as e:
        error_str = str(e)
        if "INSUFFICIENT_SCOPES" in error_str:
            print("Warning: Cannot fetch pinned repositories - continuing without them", file=sys.stderr)
        else:
            raise

    # Try to get organizations (requires read:org scope)
    orgs = []
    try:
        org_data = gql(ORGS_Q, {"login": USER_LOGIN})
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
        d2 = gql(RECENT_REPOS_Q, {"login": USER_LOGIN})
        for r in d2["user"]["repositories"]["nodes"]:
            recent.append({
              "name": r["name"],
              "description": r.get("description"),
              "url": r["url"],
              "stargazerCount": r["stargazerCount"],
              "forkCount": r["forkCount"],
              "updatedAt": r["updatedAt"],
              "primaryLanguage": r.get("primaryLanguage"),
              "topics": flatten_topics((r.get("repositoryTopics") or {}).get("nodes", [])),
            })
    except RuntimeError as e:
        error_str = str(e)
        if "INSUFFICIENT_SCOPES" in error_str:
            print("Warning: Cannot fetch recent repositories - token may need 'repo' scope", file=sys.stderr)
        else:
            raise

    with open("_data/profile.json", "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)
    with open("_data/orgs.json", "w", encoding="utf-8") as f:
        json.dump(orgs, f, ensure_ascii=False, indent=2)
    with open("_data/repos.json", "w", encoding="utf-8") as f:
        json.dump({"pinned": pinned, "recent": recent}, f, ensure_ascii=False, indent=2)

    print("Wrote _data/profile.json, _data/orgs.json, _data/repos.json")

if __name__ == "__main__":
    main()
