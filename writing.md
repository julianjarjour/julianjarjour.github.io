---
layout: base
---
<ul>
    {%assign essays = site.essays | sort: 'date' | reverse%}
    {%for essay in essays%}
    <li>
      <a class="essay" href="{{ essay.url }}">
      {{essay.title}}
      <p class="subtitle">{{essay.date|date:'%D'}}</p>
      </a>
    </li>
    {%endfor%}
</ul>
