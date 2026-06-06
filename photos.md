---
layout: base
title: photos 
---
<div class="g">
{% assign photos = site.static_files | reverse %}
{% for photo in photos %}
{% if photo.path contains '/photos/' %}
<a style="--w: {% imagesize photo.path:width %}; --h: {% imagesize photo.path:height %};" href="{{photo.path}}"><img src="{{ photo.path }}" loading="lazy" alt="image"></a>
{% endif %}
{%endfor%}
</div>
