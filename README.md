# viktorpm.github.io

Personal GitHub Pages site built with Jekyll and the `jekyll-theme-primer` theme. Displays GitHub profile, organizations, and repositories using the GitHub GraphQL API.

## How It Works

A Python script fetches data from the GitHub API and generates JSON files, which Jekyll uses to build the site:

```mermaid
graph LR
    A[GitHub API] --> B[fetch_github_data.py]
    B --> C[JSON files in _data/]
    C --> D[Jekyll build]
    D --> E[GitHub Pages]
```

## Files

- `_config.yml` - Jekyll configuration using `jekyll-theme-primer`
- `index.md` - Main page displaying profile, organizations, and repositories
- `scripts/fetch_github_data.py` - Fetches GitHub data via GraphQL API
- `_data/` - Generated JSON files (profile.json, orgs.json, repos.json)

## Usage

### Local Development

1. Install dependencies:
   ```bash
   bundle install
   ```

2. Fetch data (requires GitHub token):
   ```bash
   python3 scripts/fetch_github_data.py
   ```

3. Run locally:
   ```bash
   bundle exec jekyll serve
   ```

### Deployment

Site automatically deploys to GitHub Pages when changes are pushed to the repository.