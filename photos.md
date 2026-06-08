---
layout: base
title: photos 
---
<div class="g">
{% assign photos = site.static_files | reverse %}
{% for photo in photos %}
    {% if photo.path contains '/thumbs' %}
        {% assign small = photo.path | replace: "thumbs", "smallthumbs" | replace: "t.", "st." %}
        <a style="--w: {% imagesize photo.path:width %}; --h: {% imagesize photo.path:height %};" href="{{ photo.path | remove: "/thumbs" | replace: "t.", "." }}"><img alt="{{ photo.path | remove: "/photos/" | remove: "/thumbs/" }}" srcset="{{ small }} {% imagesize small:width %}w, {{photo.path}} {% imagesize photo.path:width %}w" sizes="(max-width:692px) 90vw,624px" src="{{ small }}" loading="lazy"></a>
    {% endif %}
{% endfor %}
</div>
