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


<h2>now <small>as of 6/3/26</small></h2>

Just wrapped up my fourth and best semester, and I'm
hoping to graduate in just two more. Currently looking
for internships in lieu of a second capstone.

The church gig has been going well; I'm diving into learning
the organ because I may be leading a service or two this
summer. I've also gotten on the roster for what functions as
my university's jazz booking agency---this has led me to
playing my very first professional, well-paying jazz gigs.
These were played on 64 unweighted keys without a sustain
pedal, but still went swimmingly. Along the way, I played
two oud gigs for National Arab American Heritage Month and
had the opportunity to perform at Boston's iconic Hatch
Shell a few days ago!

Outside of music, I've been taking it easy. I'm attending
weekly meditations at a Zen center near my church, playing
pool at the thrift shop, watching sailing documentaries,
reading Robert Pirsig, photographing basement shows, and
enjoying a hand-me-down vintage radio receiver.

I'm looking forward to a summer of yum-yummyness. I hope yours is full
of joy as well, rare reader!
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
