---
layout: base
description: I'm a 19-year-old musician and naturalist. This is where I write about what I learn and what I like.
---
<style>
.welcome{display:inline-block;font-size:5.52vw;}
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

## now <span class="subtitle">as of 1/17/25</span>

I've been really enjoying playing piano at church, it has
provided some much needed routine and it's helping me fall
back in love with the piano. On that note, I've also decided
to audition for my university jazz ensemble. Wish me luck.

My family recently acquired a pool table gratis through
Craigslist, which I've been playing on a lot. I've also been
enjoying pickleball with a couple of pals. We're running a
fantasy tennis league this year, which me and my friend Gio
are developing an app for.

I've been falling in love with fiber arts lately. I've just
finished my first crochet project: a pair of colorful
fingerless gloves which are now the warmest gloves I own. I
want to learn how to weave, sew, and knit.

Things have been pretty swell since finishing my most
stressful semester. I hope things are swell for you too.

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

<figure class="poem">
<div class="stanza">
<span class="verse">My candle burns at both ends;<br>
It will not last the night;</span><br>
<span class="verse">But ah, my foes, and oh, my friends—<br>
It gives a lovely light!</span>
</div><figcaption>Edna St. Vincent Millay</figcaption></figure>

