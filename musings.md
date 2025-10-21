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

<figure class="poem">
<div class="stanza">
<span class="verse">Safe upon the solid rock the ugly houses stand:</span><br>
<span class="verse">Come and see my shining palace built upon the sand!</span>
</div><figcaption>Edna St. Vincent Millay</figcaption></figure>
