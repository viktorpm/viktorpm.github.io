---
layout: page
title: "Projects"
permalink: /projects/
---

## Featured Projects

{% for repo in site.data.repos.pinned %}
### [{{ repo.name }}]({{ repo.url }})

{% if repo.description %}{{ repo.description }}{% endif %}

- **Language**: {{ repo.primaryLanguage.name | default: "N/A" }}
- **Stars**: {{ repo.stargazerCount }}
{% if repo.topics and repo.topics.size > 0 %}
- **Topics**: {{ repo.topics | join: ", " }}
{% endif %}

---

{% endfor %}

## Recently Updated

{% for repo in site.data.repos.recent %}
### [{{ repo.name }}]({{ repo.url }})

{% if repo.description %}{{ repo.description }}{% endif %}

- **Language**: {{ repo.primaryLanguage.name | default: "N/A" }}
- **Stars**: {{ repo.stargazerCount }}
- **Updated**: {{ repo.updatedAt | date: "%B %d, %Y" }}
{% if repo.topics and repo.topics.size > 0 %}
- **Topics**: {{ repo.topics | join: ", " }}
{% endif %}

---

{% endfor %}
