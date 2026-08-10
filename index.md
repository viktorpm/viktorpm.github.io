---
layout: default
title: "Viktor Plattner"
---

<div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
  <img src="{{ site.data.github_profile.avatarUrl }}" alt="Viktor Plattner" class="profile-image" style="width: 120px; height: 120px; border-radius: 50%; border: 3px solid var(--primary);">
  <div>
    {% if site.data.github_profile.bio %}
    {{ site.data.github_profile.bio }}
    {% else %}
    Neuroscientist working on data systems and lab infrastructure. I focus on computational neuroanatomy, behavior analysis, and building tools for neuroscience research.
    {% endif %}
  </div>
</div>

## What I Do
- **Build**: high-throughput training rigs and lab web dashboards
- **Maintain**: HPC/Servers, data pipelines (Neuropixels + SpikeInterface/Kilosort)
- **Develop**: tools for neuroscience data analysis and documentation at scale
- **Teach**: hardware and systems curriculum with [No Black Boxes](https://noblackboxes.org)
- **Collaborate**: BrainGlobe projects

## Featured Projects

{% for repo in site.data.repos.pinned limit:5 %}
- ### [{{ repo.name }}]({{ repo.url }})
    {% if repo.description %}<p style="font-size: 14px; color: var(--text-secondary); margin: -8px 0 32px 0;">{{ repo.description }}</p>{% endif %}

{% endfor %}

## Organizations

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">
{% assign sorted_orgs = site.data.orgs | sort: 'name' %}
{% for org in sorted_orgs %}
  <a href="{{ org.url }}" style="display: flex; align-items: center; gap: 15px; padding: 15px; border: 1px solid var(--border); border-radius: 8px; background: {% if org.role %}var(--surface-variant){% else %}var(--surface){% endif %}; {% if org.role %}border-left: 4px solid var(--primary);{% endif %}{% if org.login == 'LIMLabSWC' or org.login == 'NoBlackBoxes' %} order: -1;{% endif %}; text-decoration: none; color: inherit;">
    {% if org.avatarUrl %}
    <img src="{{ org.avatarUrl }}" alt="{{ org.name | default: org.login }}" style="width: 60px; height: 60px; border-radius: 8px;">
    {% endif %}
    <div>
      <h4 style="margin: 0 0 5px 0; color: var(--text-primary);">{{ org.name | default: org.login }}</h4>
      {% if org.description %}<p style="margin: 0; font-size: 14px; color: var(--text-secondary);">{{ org.description }}</p>{% endif %}
      <div style="margin-top: 5px;">
        {% if org.role %}<span style="font-size: 12px; color: var(--text-primary); font-weight: bold; background: var(--surface-variant); padding: 2px 6px; border-radius: 4px;">{% if org.login == 'LIMLabSWC' %}⚙️ {% endif %}{{ org.role }}</span>{% endif %}
        {% if org.isVerified %}<span style="font-size: 12px; color: var(--success); font-weight: bold; margin-left: 8px;">✓ Verified</span>{% endif %}
      </div>
    </div>
  </a>
{% endfor %}
</div>
