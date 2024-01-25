---
layout: base
---
<ul>
    {%assign essays = site.essays | sort: 'date' | reverse%}
    {%for essay in essays%}
    <li>
      <a class="essay" href="{{ essay.url }}">
      <div class="edt">
      {{essay.title}}
      <p class="subtitle">{{essay.date|date:'%D'}}</p>
      </div>
      <p class="essaydesc">{{essay.description}}</p>
    </a>
        </li>
    {%endfor%}
</ul>
