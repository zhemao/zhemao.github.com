---
title: Things Every Python Programmer Should Know
layout: default
---

Python is a really great programming language, and one of the many reasons
for its success is a simple, easy-to-understand syntax. That being said,
there are some things that can trip up beginners (and which have tripped me
up before). Therefore, I am attempting to document some of the common pitfalls
here.

## Efficient String Concatenation

Because Python uses immutable strings, concatenating two strings involves a
bit of overhead (as a new `str` object must be allocated each time), which
means that performing concatenations using the most obvious method will lead
to rather poor performance. For my example, let us assume we have a generator
method `genstr` which takes as input an integer n and yields a random string on 
each iteration, stopping after n number of iterations. How would one concatenate
the results of `genstr`. The most obvious way would be like so.

	{% highlight python %}
    mystr = ''
	for randstr in genstr(n):
		mystr += randstr
	{% endhighlight %}

But this is very inefficient for the reason that a new string has to be created
and assigned to mystr on each loop. What is the most efficient method of 
concatenation? List comprehension.

{% highlight python %}
	mystr = ''.join([s for s in genstr(n)])
	# or alternatively
	mystr = ''.join(s for s in genstr(n))
{% endhighlight %}

The second is actually a generator comprehension, not a list comprehension. 
They are more memory efficient (as you don't have to pre-allocate the entire
list), but are slower than list comprehensions in Python 2.x (they have 
comparable speed in Python 3). Of course, sometimes, performing a list 
comprehension is not ideal, because your inner loop might be slightly more
complicated than just returning the yielded value. In that case, the next
best way is to use a StringIO object, like so.

	{% highlight python %}
    import io

	sio = io.StringIO()

	for randstr in gen(n):
		sio.write(randstr)

	mystr = sio.getvalue()
	{% endhighlight %}

*Attribution* - this information was taken from an article written by 
[Oliver Crow](http://www.skymind.com/~ocrow/python_string/).

## Class Attributes and Default Parameters

Two sources of endless confusion and bugs in Python come from a misunderstanding
of the scope of class attributes and default parameters for functions. A class
attribute looks like the following.

	{% highlight python %}
	class A:
		a = 'blah'
	{% endhighlight %}

A default parameter looks like this.
	
	{% highlight python %}
	def something(a = 'blah'):
		pass
	{% endhighlight %}

Class attributes are bound when the class is created, and default parameters
are bound when the function is created. Mutating the state of class attributes
will change the attribute in all instances of a class. Mutating the state of a
default parameter will cause that change to persist in all future calls of the
function. This means that both of the following should be avoiding.

	{% highlight python %}
	class A:
		a = []
	
	b = A()
	c = A()
	b.a.append('blah')
	# now b.a and c.a are both ['blah']

	def something(a = []):
		a.append('blah')
		return a

	# calling something without arguments 5 times will cause 'blah' to show up
	# 5 times in the returned list
	{% endhighlight %}

Instead, do it like this.

	{% highlight python %}
	class A:
		def __init__(self):
			self.a = []
			self.a.append('blah')

	def something(a = None):
		if a==None: a = []
		a.append('blah')
	{% endhighlight %}

