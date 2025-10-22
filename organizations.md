---
layout: single
title: "Organizations"
author_profile: true
permalink: /organizations/
---

## Organizations I'm part of

{% for org in site.data.orgs %}
### [{{ org.name | default: org.login }}]({{ org.url }})

{% if org.avatarUrl %}
![{{ org.login }}]({{ org.avatarUrl }})
{% endif %}

{% if org.description %}{{ org.description }}{% endif %}

{% if org.isVerified %}
**Verified Organization**
{% endif %}

---

{% endfor %}
