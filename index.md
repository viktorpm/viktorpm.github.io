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

  <section>
    <h2>Organizations</h2>
    <div class="org-grid">
    {% for org in site.data.orgs %}
      <a class="card" href="{{ org.url }}">
        {% if org.avatarUrl %}<img src="{{ org.avatarUrl }}" alt="{{ org.login }}" style="width: 48px; height: 48px; border-radius: 6px; float: left; margin-right: 1rem;">{% endif %}
        <div style="overflow: hidden;">
          <h3 style="margin-top: 0;">{{ org.name | default: org.login }}</h3>
          {% if org.isVerified %}<span style="background: #28a745; color: white; padding: 0.2rem 0.4rem; border-radius: 3px; font-size: 0.8rem;">✓ Verified</span>{% endif %}
          {% if org.description %}<p style="color: #666; margin-bottom: 0;">{{ org.description }}</p>{% endif %}
        </div>
      </a>
    {% endfor %}
    </div>
  </section>

  <section>
    <h2>Featured Projects</h2>
    <div class="project-grid">
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
  </section>

  <section>
    <h2>Recently Updated</h2>
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
  </section>
