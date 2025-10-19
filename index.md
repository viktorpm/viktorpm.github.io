---
layout: page
title: "Home"
---

<!-- HERO -->
<div class="hero">
  <img class="avatar" src="{{ site.data.profile.avatarUrl }}" alt="avatar">
  <div>
    <h1>{{ site.data.profile.name | default: site.data.profile.login }}</h1>
    {% if site.data.profile.bio %}<p class="muted">{{ site.data.profile.bio }}</p>{% endif %}
    <p class="muted">
      {% if site.data.profile.company %}{{ site.data.profile.company }} · {% endif %}
      {% if site.data.profile.location %}{{ site.data.profile.location }}{% endif %}
      {% if site.data.profile.websiteUrl %} · <a href="{{ site.data.profile.websiteUrl }}">website</a>{% endif %}
    </p>
  </div>
</div>

## Organizations
<div class="card-grid">
{% for org in site.data.orgs %}
  <a class="card" href="{{ org.url }}">
    <div class="card-row">
      {% if org.avatarUrl %}<img class="org-avatar" src="{{ org.avatarUrl }}" alt="{{ org.login }}">{% endif %}
      <div>
        <h3>{{ org.name | default: org.login }}</h3>
        {% if org.isVerified %}<span class="badge">Verified</span>{% endif %}
        {% if org.description %}<p class="muted">{{ org.description }}</p>{% endif %}
      </div>
    </div>
  </a>
{% endfor %}
</div>

## Featured Projects
<div class="card-grid">
{% for repo in site.data.repos.pinned %}
  <a class="card" href="{{ repo.url }}">
    <h3>{{ repo.name }}</h3>
    {% if repo.description %}<p class="muted">{{ repo.description }}</p>{% endif %}
    <p class="tiny muted">
      ⭐ {{ repo.stargazerCount }}{% if repo.primaryLanguage %} · {{ repo.primaryLanguage.name }}{% endif %}
    </p>
    {% if repo.topics and repo.topics.size > 0 %}
      <p class="tags">
        {% for t in repo.topics %}<span class="tag">{{ t }}</span>{% endfor %}
      </p>
    {% endif %}
  </a>
{% endfor %}
</div>

## Recently Updated
<div class="list">
{% for repo in site.data.repos.recent %}
  <div class="list-item">
    <div>
      <a href="{{ repo.url }}"><strong>{{ repo.name }}</strong></a>
      {% if repo.description %}<div class="muted">{{ repo.description }}</div>{% endif %}
      <div class="tiny muted">
        Updated {{ repo.updatedAt | date: "%Y-%m-%d" }} · ⭐ {{ repo.stargazerCount }}{% if repo.primaryLanguage %} · {{ repo.primaryLanguage.name }}{% endif %}
      </div>
      {% if repo.topics and repo.topics.size > 0 %}
        <p class="tags">
          {% for t in repo.topics %}<span class="tag">{{ t }}</span>{% endfor %}
        </p>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>
