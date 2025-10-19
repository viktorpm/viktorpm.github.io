---
layout: default
title: "Home"
---

<div class="container-lg px-3 my-5">

{% if site.data.profile.avatarUrl %}
<div class="text-center mb-4">
  <img class="circle" src="{{ site.data.profile.avatarUrl }}" alt="Avatar" width="120" height="120">
  <h1 class="text-center">{{ site.data.profile.name | default: site.data.profile.login }}</h1>
  {% if site.data.profile.bio %}<p class="text-center text-gray mb-4">{{ site.data.profile.bio }}</p>{% endif %}
</div>
{% endif %}

<h2 class="border-bottom pb-2">Organizations</h2>
<div class="gutter-sm">
{% for org in site.data.orgs %}
<div class="py-2 border-bottom">
  <div class="d-flex flex-items-center">
    {% if org.avatarUrl %}<img class="mr-3" src="{{ org.avatarUrl }}" alt="{{ org.login }}" width="32" height="32">{% endif %}
    <div class="flex-auto">
      <h3 class="mb-1"><a href="{{ org.url }}">{{ org.name | default: org.login }}</a></h3>
      {% if org.description %}<p class="text-gray text-small mb-1">{{ org.description }}</p>{% endif %}
      {% if org.isVerified %}<span class="Label Label--success">Verified</span>{% endif %}
    </div>
  </div>
</div>
{% endfor %}
</div>

<h2 class="border-bottom pb-2 mt-4">Featured Projects</h2>
<div class="gutter-sm">
{% for repo in site.data.repos.pinned %}
<div class="py-2 border-bottom">
  <h3 class="mb-1"><a href="{{ repo.url }}">{{ repo.name }}</a></h3>
  {% if repo.description %}<p class="text-gray mb-2">{{ repo.description }}</p>{% endif %}
  <div class="text-small text-gray">
    ⭐ {{ repo.stargazerCount }}{% if repo.primaryLanguage %} · {{ repo.primaryLanguage.name }}{% endif %}
  </div>
  {% if repo.topics and repo.topics.size > 0 %}
    <div class="mt-2">
      {% for t in repo.topics %}<span class="IssueLabel mr-1">{{ t }}</span>{% endfor %}
    </div>
  {% endif %}
</div>
{% endfor %}
</div>

<h2 class="border-bottom pb-2 mt-4">Recently Updated</h2>
<div class="gutter-sm">
{% for repo in site.data.repos.recent %}
<div class="py-2 border-bottom">
  <h3 class="mb-1"><a href="{{ repo.url }}">{{ repo.name }}</a></h3>
  {% if repo.description %}<p class="text-gray mb-2">{{ repo.description }}</p>{% endif %}
  <div class="text-small text-gray">
    Updated {{ repo.updatedAt | date: "%Y-%m-%d" }} · ⭐ {{ repo.stargazerCount }}{% if repo.primaryLanguage %} · {{ repo.primaryLanguage.name }}{% endif %}
  </div>
  {% if repo.topics and repo.topics.size > 0 %}
    <div class="mt-2">
      {% for t in repo.topics %}<span class="IssueLabel mr-1">{{ t }}</span>{% endfor %}
    </div>
  {% endif %}
</div>
{% endfor %}
</div>

</div>
