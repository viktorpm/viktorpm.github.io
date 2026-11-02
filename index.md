---
layout: default
title: "Viktor Plattner"
---

<div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
  <a class="profile-link" href="{{ site.data.github_profile.url }}" aria-label="Visit Viktor's GitHub profile">
    <img src="{{ site.data.github_profile.avatarUrl }}" alt="" class="profile-image" style="width: 120px; height: 120px; border-radius: 50%; border: 3px solid var(--primary);">
    <span class="profile-github-badge" aria-hidden="true">
      <svg viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
        <path fill="currentColor" d="M6.766 11.328c-2.063-.25-3.516-1.734-3.516-3.656 0-.781.281-1.625.75-2.188-.203-.515-.172-1.609.063-2.062.625-.078 1.468.25 1.968.703.594-.187 1.219-.281 1.985-.281.765 0 1.39.094 1.953.265.484-.437 1.344-.765 1.969-.687.218.422.25 1.515.046 2.047.5.593.766 1.39.766 2.203 0 1.922-1.453 3.375-3.547 3.64.531.344.89 1.094.89 1.954v1.625c0 .468.391.734.86.547C13.781 14.359 16 11.53 16 8.03 16 3.61 12.406 0 7.984 0 3.563 0 0 3.61 0 8.031a7.88 7.88 0 0 0 5.172 7.422c.422.156.828-.125.828-.547v-1.25c-.219.094-.5.156-.75.156-1.031 0-1.64-.562-2.078-1.609-.172-.422-.36-.672-.719-.719-.187-.015-.25-.093-.25-.187 0-.188.313-.328.625-.328.453 0 .844.281 1.25.86.313.452.64.655 1.031.655s.641-.14 1-.5c.266-.265.47-.5.657-.656"/>
      </svg>
    </span>
  </a>
  <div>
    I work across neuroscience research and hands-on technical education.
  </div>
</div>

## What I Do
- **Teach and develop** practical hardware and systems courses through [No Black Boxes](https://noblackboxes.org)
- **Build** tools, workflows, and infrastructure for neuroscience research, including lab dashboards and training systems
- **Contribute** to BrainGlobe's open-source computational neuroanatomy tools

## Featured Projects

{% for repo in site.data.repos.pinned limit:5 %}
- ### [{{ repo.name }}]({{ repo.url }})
    {% if repo.description %}<p style="font-size: 14px; color: var(--text-secondary); margin: -8px 0 32px 0;">{{ repo.description }}</p>{% endif %}

{% endfor %}

## Organizations

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">
{% assign sorted_orgs = site.data.orgs | sort: 'name' %}
{% for org in sorted_orgs %}
  <a class="organization-card" href="{{ org.url }}" style="display: flex; align-items: center; gap: 15px; padding: 15px; border: 1px solid var(--border); border-radius: 8px; background: {% if org.role %}var(--surface-variant){% else %}var(--surface){% endif %}; {% if org.role %}border-left: 4px solid var(--primary);{% endif %}{% if org.login == 'NoBlackBoxes' %} order: -2;{% elsif org.login == 'LIMLabSWC' %} order: -1;{% endif %}; text-decoration: none; color: inherit;">
    {% if org.avatarUrl %}
    <img src="{{ org.avatarUrl }}" alt="{{ org.name | default: org.login }}" style="width: 60px; height: 60px; border-radius: 8px;">
    {% endif %}
    <div>
      <h4 style="margin: 0 0 5px 0; color: var(--text-primary);">{{ org.name | default: org.login }}</h4>
      {% if org.description %}<p style="margin: 0; font-size: 14px; color: var(--text-secondary);">{{ org.description }}</p>{% endif %}
      <div style="margin-top: 5px;">
        {% if org.role %}<span style="font-size: 12px; color: var(--text-primary); font-weight: bold; background: var(--surface-variant); padding: 0px 0px; border-radius: 0px;">{% if org.login == 'LIMLabSWC' %}{% endif %}{{ org.role }}</span>{% endif %}
      </div>
    </div>
  </a>
{% endfor %}
</div>
