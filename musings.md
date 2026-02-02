---
layout: base
title: musings 
---
{%assign posts = site.musings| sort: 'date' | reverse %}
{%for post in posts%}
<article>
  <a class="post" href="{{post.url}}">
  <p>{{post.title}}</p>
  <small>{{post.date|date:'%D'}}</small>
  </a>
</article>
{%endfor%}
