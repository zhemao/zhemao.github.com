---
title: Cyclone V Series
layout: default
category: project
---

This is a series of blog posts about FPGA and embedded Linux development on the
[Arrow SoCKit evaluation board](http://www.arrownac.com/solutions/sockit/).
The SoCKit contains a Cyclone V SoC, which combines an Altera FPGA with
a dual-core ARM Cortex A9 hard processor. The ARM processor is able to run
embedded Linux distributions, making the Cyclone V ideal for projects that
combine the excellent software support of Linux with the parallel processing
capabilities and precise timing control of the FPGA.
The posts in the series focus on programming the FPGA in Verilog and
interfacing the FPGA with Linux kernel modules and userspace programs running
on the ARM processor using Altera's Qsys system integration tool.

<ul class="front-page-list">
{% for post in site.categories.fpga reversed %}
<li><a href="{{post.url}}">{{post.title}}</a></li>
{% endfor %}
</ul>
