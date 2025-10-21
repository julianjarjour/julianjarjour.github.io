---
layout: base
---
<style>
.welcome{display:inline-block;font-size:4.98vw;}
@media (min-width:662px){.welcome{font-size:145%;}}
@media (max-width:345px){.welcome{font-size:4.8vw;}}
</style>
<div class="welcome"> <figure><img
src="julian-portrait.webp" width="624" height="832" alt="Me and my black cat Bisi."
style="float:left;shape-outside:url(julian-portrait.webp);shape-margin:1.5rem;"></figure>
I'm a
{{"now"|date:"%Y%m%d"|minus:"20060713"|slice:0,2}}-year-old
musician and student of nature. This is where I write about
what I learn and what I like.</div> <figcaption
style="float:right;">me and Bisi</figcaption>

## latest posts

<ul>
    {%assign posts = site.musings| sort: 'date' | reverse %}
    {%for post in posts limit: 3%}
    <li>
      <a class="post" href="{{post.url}}">
      <p class="mpt">{{post.title}}</p>
      <p class="subtitle pd">{{post.date|date:'%D'}}</p>
      </a>
    </li>
    {%endfor%}
</ul>

