---
layout: default
---

I am a recent graduate of Columbia University, where I studied Computer Engineering.
My interests are in digital hardware design, FPGA prototyping, embedded
systems, Linux kernel hacking, systems programming, and parallel computing.

You can find some of my code on [Github](https://github.com/zhemao) 
and [Bitbucket](https://bitbucket.org/zhemao). I have some videos of my
hardware projects on [Youtube](http://www.youtube.com/zhemaoce).

## Blog Pages
{% for post in site.categories.blog %}
* [{{post.title}}]({{post.url}})
{% endfor %}

## Projects
{% for post in site.categories.project %}
* [{{post.title}}]({{post.url}})
{% endfor %}
