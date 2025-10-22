---
layout: page
title: "Viktor Plattner"
---

{% if site.data.github_profile.bio %}
{{ site.data.github_profile.bio }}
{% else %}
Neuroscientist working on data systems and lab infrastructure. I focus on computational neuroanatomy, behavior analysis, and building tools for neuroscience research.
{% endif %}

## What I Do

- **Research**: Computational neuroanatomy and motor control
- **Tools**: Building software for neuroscience data analysis
- **Infrastructure**: Lab systems and high-throughput behavior training
- **Collaboration**: Working with organizations like BrainGlobe and Sainsbury Wellcome Centre

## Contact

- **GitHub**: [{{ site.data.github_profile.login }}]({{ site.data.github_profile.url }})
{% if site.data.github_profile.websiteUrl %}
- **Website**: [{{ site.data.github_profile.websiteUrl }}]({{ site.data.github_profile.websiteUrl }})
{% endif %}
{% if site.data.github_profile.location %}
- **Location**: {{ site.data.github_profile.location }}
{% endif %}
{% if site.data.github_profile.company %}
- **Company**: {{ site.data.github_profile.company }}
{% endif %}
