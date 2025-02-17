---
layout: base
title: musings 
---
<ul>
    {%assign posts = site.musings| sort: 'date' | reverse %}
    {%for post in posts%}
    <li>
      <a class="post" href="{{post.url}}">
      <p class="mpt">{{post.title}}</p>
      <p class="subtitle pd">{{post.date|date:'%D'}}</p>
      </a>
    </li>
    {%endfor%}
</ul>
