# viktorpm.github.io

A personal GitHub Pages site built with Jekyll that dynamically displays GitHub profile information, organizations, and repositories using the GitHub GraphQL API.

## Architecture Overview

This repository uses a completely prebuilt theme approach with zero custom styling:

> **Note**: Uses GitHub's `jekyll-theme-primer` theme with no custom CSS. All styling comes from the built-in theme.

```
viktorpm.github.io/
├── 📁 Data Pipeline
│   ├── scripts/fetch_github_data.py  # GitHub API data fetcher
│   └── _data/                   # Generated JSON data files
└── 📁 Jekyll Core
    ├── _config.yml              # Site configuration (jekyll-theme-primer)
    ├── index.md                 # Main page content (Theme-native HTML)
    └── Gemfile                  # Ruby dependencies
```

## How It Works

### 1. Data Flow

```mermaid
graph TD
    A[GitHub GraphQL API] -->|Manual| B[fetch_github_data.py]
    B --> C[_data/profile.json]
    B --> D[_data/orgs.json]
    B --> E[_data/repos.json]
    C --> F[Jekyll Site Build]
    D --> F
    E --> F
    F --> G[GitHub Pages]
```

**Data Sources:**
- **Profile Data**: User name, bio, location, avatar, etc.
- **Organizations**: Organizations the user belongs to
- **Repositories**: Pinned repos and recently updated repos

### 2. Component Architecture

#### Frontend (Jekyll + Primer Theme)
- **Base Theme**: `jekyll-theme-primer` (GitHub's official theme)
- **No Custom Styling**: Uses only built-in theme classes and components
- **Layout**: Single-page design with GitHub-style components

#### Data Layer
- **Python Script**: `scripts/fetch_github_data.py`
  - Interactive token prompting for local development
  - Graceful error handling for insufficient API scopes
  - Generates structured JSON data for Jekyll consumption

#### Build System
- **Jekyll**: Static site generator with Primer theme
- **No Custom Assets**: All styling from theme
- **GitHub Pages**: Automatic build and deployment

## File Structure & Responsibilities

### Core Configuration

**`_config.yml`** - Jekyll site configuration
```yaml
title: "Viktor Plattner"
description: "Neuroscientist • Data/Systems • Lab Infrastructure"
theme: jekyll-theme-primer
markdown: kramdown
```

**`Gemfile`** - Ruby dependencies
```ruby
# Gemfile for viktorpm.github.io
# Ensures compatibility with GitHub Pages hosting

source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
gem "webrick", "~> 1.7"
```

### Theme Architecture

**Built-in Theme Styling** - Uses jekyll-theme-primer components
```html
<!-- GitHub-style components from actual index.md -->
<div class="container-lg px-3 my-5">
<div class="d-flex flex-items-center">
  <img class="mr-3" src="..." alt="org" width="32" height="32">
  <span class="Label Label--success">Verified</span>
</div>
<span class="IssueLabel mr-1">tag</span>
```

- Uses only GitHub's Primer theme classes from the actual implementation
- No custom CSS or SCSS files
- Automatic responsive design and GitHub styling

### Data Pipeline

**`scripts/fetch_github_data.py`** - GitHub API integration
```python
# Features:
# - Interactive token prompting (secure)
# - Graceful scope error handling
# - Modular GraphQL queries
# - Robust error reporting
```

Generated data files:
- `_data/profile.json` - User profile information
- `_data/orgs.json` - Organization membership data
- `_data/repos.json` - Repository data (pinned + recent)

### Content Structure

**`index.md`** - Main page template (actual structure)
```liquid
---
layout: default
title: "Home"
---

<div class="container-lg px-3 my-5">
<!-- Profile avatar and name -->
<!-- Organizations section with d-flex layout -->
<!-- Featured Projects with repo cards -->
<!-- Recently Updated repos -->
</div>
```

### Content Updates

Data updates can be triggered by running the Python script manually:
```bash
python3 scripts/fetch_github_data.py
```

## Key Features

### 🔐 Security
- Interactive token prompting (no hardcoded secrets)
- Proper `.gitignore` for sensitive files

### 🎨 Design
- Clean, professional aesthetic
- Responsive design for all devices
- Dark mode support via CSS media queries
- Consistent typography and spacing

### 🛠️ Maintainability
- No custom CSS files or theme overrides
- Well-documented code with clear section headers
- Clean HTML structure using theme classes only

### ⚡ Performance
- Static site generation for fast loading
- Built-in theme CSS (no additional imports needed)
- GitHub Pages native hosting

### 🔄 Content Updates
- Manual data fetching via Python script
- Automatic GitHub Pages deployment on push

## Setup & Usage

### Local Development

1. **Clone and setup dependencies**:
   ```bash
   git clone https://github.com/viktorpm/viktorpm.github.io.git
   cd viktorpm.github.io
   bundle install
   ```

2. **Fetch initial data**:
   ```bash
   python3 scripts/fetch_github_data.py
   # Enter your GitHub token when prompted
   ```

3. **Run locally**:
   ```bash
   bundle exec jekyll serve
   # Site available at http://127.0.0.1:4000
   ```

### Production Deployment

The site automatically deploys to GitHub Pages when you push changes to the repository.

### Required Setup

1. **GitHub Pages**: 
   - Enable Pages in repository settings
   - Select source branch (typically `main`)

2. **For Manual Data Updates**: 
   - You can run the data fetching script locally and commit the updated JSON files

## Maintenance Guide

### Adding New Content Types
1. Update `fetch_github_data.py` with new GraphQL query
2. Add corresponding JSON data structure
3. Update `index.md` template to display new data using Primer theme classes

### Styling Changes
- Use GitHub's Primer theme utility classes (no custom CSS)
- Reference Primer documentation for available components
- Maintain clean HTML structure with theme classes

### Updating Dependencies
- Modify `Gemfile` for Ruby gems
- Update Python script dependencies as needed
- Test locally before pushing changes

## Technology Stack

- **Jekyll**: Static site generator
- **Primer Theme**: GitHub's official theme (no custom CSS)
- **Python**: GitHub API data fetching
- **GitHub GraphQL API**: Data source
- **GitHub Pages**: Automated hosting and deployment

## Repository Status

The repository is currently in a clean, maintainable state:

- ✅ **No leftover files**: Clean structure with only necessary files
- ✅ **Zero custom CSS**: Uses only built-in Primer theme styling
- ✅ **Theme-native HTML**: Uses proper GitHub theme components
- ✅ **Clean structure**: No empty directories or unused files
- ✅ **Well-documented**: All files have clear headers and comments
- ✅ **Security**: Interactive token prompting, proper `.gitignore`

## Contributing

This is a personal site, but the architecture is designed for maintainability. Key principles:
- Keep customizations clean and documented
- Avoid theme overrides that could break on updates
- Use proper Jekyll extension mechanisms
- Maintain security best practices for API tokens
