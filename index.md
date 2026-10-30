---
layout: default
title: "Viktor Plattner"
---

<div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
  <img src="{{ site.data.github_profile.avatarUrl }}" alt="Viktor Plattner" class="profile-image" style="width: 120px; height: 120px; border-radius: 50%; border: 3px solid var(--primary);">
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
