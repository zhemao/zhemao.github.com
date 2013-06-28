---
title: Playing Audio from the Arduino
layout: default
---

Recently, I've been experimenting with playing audio from my Arduino.
At first, I was using one of those crappy Radio Shack piezo buzzers.
After a while, I got tired of their high-pitched squealing and decided to
try playing the audio on a regular speaker.

At this point, I encountered a problem. It's not entirely obvious how you
would hook up wires from the Arduino to the analog audio jack from a standard
speaker. At first glance, the audio jack just looks like a single piece of
metal. So where do you put the signal and where do you put ground?

Turns out, the audio jack is actually three distinct pieces of metal separated
by two black insulating bands. The piece of metal at the base is ground, the
ring in the middle is the right channel audio, and the tip is the left
channel audio (assuming you have a stereo speaker). 

![Audio Jack Diagram](/images/audio-jack.png)

So, I hooked a wire from the base to ground, hooked a resistor from the tip to 
pin 8, and then ran the [tone](http://arduino.cc/en/Tutorial/Tone) example
from the Arduino website. [Here](http://youtu.be/vuev2IG9LZ4) is the result.

<iframe width="560" height="315" src="http://www.youtube.com/embed/vuev2IG9LZ4" 
    frameborder="0">Youtube Embedding Disabled</iframe>
