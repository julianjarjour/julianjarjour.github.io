---
layout: base
description: I'm a 19-year-old musician and naturalist. This is where I write about what I learn and what I like.
---
<style>
.welcome{display:inline-block;font-size:5.55vw;}
@media (min-width:692px){.welcome{font-size:1.55rem;}}
</style>
<div class="welcome"> <figure><img
src="julian-portrait.webp" fetchpriority="high" width="624" height="832" alt="Me and my black cat Bisi."
style="float:left;shape-outside:polygon(25% 0%, 32% 11%, 35% 12%, 47% 38%, 67% 35%, 82% 55%, 100% 70%, 100% 100%, 0% 100%, 0% 0%);"></figure>
I'm a
{{"now"|date:"%Y%m%d"|minus:"20060713"|slice:0,2}}-year-old
musician and naturalist. This is where I write about
what I learn and what I like.</div> <figcaption
style="float:right;">me and Bisi</figcaption>

## [latest posts](/musings.html)

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

## now <span class="subtitle">as of 10/21/25</span>

Stumbled into a church piano gig, sparking my return to the instrument after a 1.5 year hiatus. Trying to disconnect from this virtual insanity. Reading about love, solitude, and the history of Syria.
