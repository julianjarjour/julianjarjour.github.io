---
layout: base
description: I'm a 19-year-old musician and naturalist. This is where I write about what I learn and what I like.
---
<div class="welcome"><img
src="julian-portrait.webp" fetchpriority="high" width="624" height="832" alt="Me and my black cat Bisi."
style="float:left;shape-outside:polygon(25% 0%, 32% 11%, 35% 12%, 47% 38%, 67% 37%, 82% 55%, 100% 70%, 100% 100%, 0% 100%, 0% 0%);">
I'm a {{"now"|date:"%Y%m%d"|minus:"20060713"|slice:0,2}}-year-old musician and naturalist writing about what I learn and what I like.
<div class="bisi">And this is<br>my cat Bisi.</div>
</div>


<h2>now <small>as of 1/24/25</small></h2>

I am reunited and once again enamored with the piano thanks
to my lovely church gig. It's inspired me to audition for my
university jazz ensemble, and the audition went swimmingly.
I'm back on the grind.

Started playing pool on my new eight-foot table, which I
acquired for free off Craigslist. I've also been enjoying
pickleball with a couple of friends. We're running a
fantasy tennis league this year, which I'm helping to
develop an app for.

I've been falling in love with fiber arts lately. I've just
finished my first crochet project: a pair of colorful
fingerless gloves which are now the warmest gloves I own.
I'd love to learn how to weave, sew, and knit.

My winter break has come to an end, but it's been pretty swell.
I hope things are swell with you too.

## [latest posts](/musings.html)

{%assign posts = site.musings| sort: 'date' | reverse %}
{%for post in posts limit: 3%}
<article>
  <a class="post" href="{{post.url}}">
  <p>{{post.title}}</p>
  <small>{{post.date|date:'%D'}}</small>
  </a>
</article>
{%endfor%}
