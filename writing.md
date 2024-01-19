---
layout: base
---
{% assign essays = site.essays | sort: 'date' | reverse %}
<ul>
  {% for essay in essays %}
    <li class="essay">
    <div class="essaytitledate">
      <a href="{{ essay.url }}">{{ essay.title }}</a>
      <p class="subtitle">{{ essay.date | date: '%b %-d, %Y' }}</p>
      </div>
      <p>{{essay.description}}</p>
    </li>
  {% endfor %}
</ul>
