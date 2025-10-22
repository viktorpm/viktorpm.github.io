---
layout: page
title: "About"
---

## Viktor Plattner

{% if site.data.profile.bio %}
{{ site.data.profile.bio }}
{% else %}
Neuroscientist working on data systems and lab infrastructure. I focus on computational neuroanatomy, behavior analysis, and building tools for neuroscience research.
{% endif %}

## What I Do

- **Research**: Computational neuroanatomy and motor control
- **Tools**: Building software for neuroscience data analysis
- **Infrastructure**: Lab systems and high-throughput behavior training
- **Collaboration**: Working with organizations like BrainGlobe and Sainsbury Wellcome Centre

## Contact

- **GitHub**: [{{ site.data.profile.login }}]({{ site.data.profile.url }})
{% if site.data.profile.websiteUrl %}
- **Website**: [{{ site.data.profile.websiteUrl }}]({{ site.data.profile.websiteUrl }})
{% endif %}
{% if site.data.profile.location %}
- **Location**: {{ site.data.profile.location }}
{% endif %}
{% if site.data.profile.company %}
- **Company**: {{ site.data.profile.company }}
{% endif %}

## Quick Links

- **[Projects](/projects/)** - Featured repositories and recent work
- **[Organizations](/organizations/)** - Research groups and collaborations
