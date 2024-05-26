---
layout: base
---
<ul>
    {%assign writing = site.writing | sort: 'date' | reverse %}
    {%for post in writing%}
    <li>
      <a class="post" href="{{ post.url }}">
      {{post.title}}
      <p class="subtitle">{{post.date|date:'%D'}}</p>
      </a>
    </li>
    {%endfor%}
</ul>
