# viktorpm.github.io

A personal GitHub Pages site built with Jekyll that dynamically displays GitHub profile information, organizations, and repositories using the GitHub GraphQL API.

## Architecture Overview

This repository uses a simplified, robust architecture built on GitHub Pages native themes and minimal customizations:

> **Note**: This simplified approach uses Jekyll's `minima` theme with proper SCSS styling for maintainability and reliability.

```
viktorpm.github.io/
├── 📁 Data Pipeline
│   ├── scripts/fetch_github_data.py  # GitHub API data fetcher (CI + local modes)
│   └── _data/                   # Generated JSON data files
├── 📁 Jekyll Core
│   ├── _config.yml              # Site configuration (minima theme)
│   ├── index.md                 # Main page content (clean HTML + CSS classes)
│   ├── assets/css/style.scss    # Custom SCSS styles
│   └── Gemfile                  # Ruby dependencies
└── 📁 Data
    └── _data/                   # Generated JSON data files
```

## How It Works

### 1. Data Flow

```mermaid
graph TD
    A[GitHub GraphQL API] -->|Daily/Auto| B[fetch_github_data.py]
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

#### Frontend (Jekyll + Minima Theme)
- **Base Theme**: `minima` (Jekyll's default theme)
- **Custom Styling**: Clean SCSS organized in `assets/css/style.scss`
- **Layout**: Single-page design with hero section and organized content blocks

#### Data Layer
- **Python Script**: `scripts/fetch_github_data.py`
  - Automatic token detection (CI vs local modes)
  - Graceful error handling for insufficient API scopes
  - Generates structured JSON data for Jekyll consumption

#### Build System
- **Jekyll**: Static site generator with minima theme
- **SCSS Pipeline**: Clean, maintainable stylesheets
- **GitHub Pages**: Automatic build and deployment

## File Structure & Responsibilities

### Core Configuration

**`_config.yml`** - Jekyll site configuration
```yaml
title: "Viktor Plattner"
description: "Neuroscientist • Data/Systems • Lab Infrastructure"
theme: minima
markdown: kramdown
```

**`Gemfile`** - Ruby dependencies
```ruby
# github-pages gem for GitHub Pages compatibility
# webrick for Ruby 3+ support
```

### Styling Architecture

**`assets/css/style.scss`** - Custom styles extending minima
```scss
@import "minima";

// Custom component styles
.hero { /* styles */ }
.card { /* styles */ }
.org-grid, .project-grid { /* styles */ }
```

- Clean, maintainable SCSS without inline styles
- Proper semantic CSS classes for all components
- Organized structure with nested selectors

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

**`index.md`** - Main page template
```liquid
<!-- Hero section with profile display -->
<!-- Organizations grid -->
<!-- Featured projects grid -->
<!-- Recently updated list -->
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
- Repository secrets for CI/CD

### 🎨 Design
- Clean, professional aesthetic
- Responsive design for all devices
- Dark mode support via CSS media queries
- Consistent typography and spacing

### 🛠️ Maintainability
- No fragile theme overrides or `!important` hacks
- Well-documented code with clear section headers
- Proper Jekyll asset pipeline usage
- Modular SCSS architecture

### ⚡ Performance
- Static site generation for fast loading
- Optimized CSS with proper imports
- GitHub Pages native hosting

### 🔄 Automation
- Daily content updates via GitHub Actions
- Manual deployment triggers
- Automated dependency management

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
3. Update `index.md` template to display new data
4. Add styles in `assets/css/style.scss` if needed

### Styling Changes
- Edit `assets/css/style.scss` for custom styles
- Follow existing section organization with nested SCSS
- Test responsive design and maintain clean structure

### Updating Dependencies
- Modify `Gemfile` for Ruby gems
- Update Python script dependencies as needed
- Test locally before pushing changes

## Technology Stack

- **Jekyll**: Static site generator
- **Minima Theme**: Jekyll's default theme (extended)
- **SCSS**: CSS preprocessing
- **Python**: GitHub API data fetching
- **GitHub GraphQL API**: Data source
- **GitHub Pages**: Automated hosting and deployment

## Repository Status

The repository is currently in a clean, maintainable state:

- ✅ **No leftover files**: Clean structure with only necessary files
- ✅ **Proper SCSS architecture**: All styles consolidated in `assets/css/style.scss`
- ✅ **No inline styles**: All styling moved to proper CSS classes
- ✅ **Clean HTML**: Semantic structure without mixed styling approaches
- ✅ **Well-documented**: All files have clear headers and comments
- ✅ **Security**: Interactive token prompting, proper `.gitignore`

## Contributing

This is a personal site, but the architecture is designed for maintainability. Key principles:
- Keep customizations clean and documented
- Avoid theme overrides that could break on updates
- Use proper Jekyll extension mechanisms
- Maintain security best practices for API tokens
