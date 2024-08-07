---
layout: base
---
<ul>
    {% assign projects = site.projects | sort: 'date' | reverse %}
    {% for post in projects%}
    <li>
      <a class="post" href="{{ post.url }}">
      {{post.title}}
      <p class="subtitle">{{post.date|date:'%D'}}</p>
      </a>
    </li>
    {%endfor%}
</ul>
