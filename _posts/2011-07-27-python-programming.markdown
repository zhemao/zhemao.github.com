---
title: Things Every Python Programmer Should Know but Generally Don't
layout: post 
---

Python is a really great programming language, and one of the many reasons
for its success is a simple, easy-to-understand syntax. That being said,
there are some things that can trip up beginners (and which have tripped me
up before). There are also a few little known features that turn out to be 
rather useful. I am attempting to document some of the common pitfalls and
esoteric-but-useful features here.

## Efficient String Concatenation

Because Python uses immutable strings, concatenating two strings involves a
bit of overhead (as a new `str` object must be allocated each time), which
means that performing concatenations using the most obvious method will lead
to rather poor performance. For my example, let us assume we have a 
generator method `genstr` which takes as input an integer n and yields a 
random string on each iteration, stopping after n number of iterations. 
How would one concatenate the results of `genstr`. The most obvious way 
would be like so.

{% highlight python %}
mystr = ''
for randstr in genstr(n):
    mystr += randstr
{% endhighlight %}

But this is very inefficient for the reason that a new string has to be 
created and assigned to mystr on each loop. What is the most efficient 
method of concatenation? List comprehension.

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

Two sources of endless confusion and bugs in Python come from a 
misunderstanding of the scope of class attributes and default parameters 
for functions. A class attribute looks like the following.

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
are bound when the function is created. Mutating the state of class 
attributes will change the attribute in all instances of a class. Mutating 
the state of a default parameter will cause that change to persist in all 
future calls of the function. This means that both of the following should 
be avoided.

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

## Multiline Strings

One of the nice features of Python is the ability to have multiline string 
literals. The canonical way of doing this is the docstring, which looks like

{% highlight python %}
'''This is a string
that spans two lines.'''
{% endhighlight %}

But I just learned recently that it can also be achieved like so.

{% highlight python %}
("This is another string "
"that is declared on two lines.")
{% endhighlight %}

So what is the difference? In a docstring, all newlines and whitespace are
preserved, in the second declaration, only the parts inside the quotes are 
rendered into the final string. Therefore, the first string when printed out
looks like.

	This is a string
	that spans two lines.

While the second will simply be

	This is another string that is declared on two lines.

If you don't want the newlines to show up as-is, the second type of 
declaration could be very useful.

## Sets

The `list`, `dict`, and `tuple` builtin classes in Python are rather 
well-known. The `set` and `frozenset` classes, not so much. A set in Python 
represents the mathematical concept of a set. It is an unordered container 
with unique elements. A frozenset has the same interface as a set, but is 
immutable, like a tuple. A set and a frozenset are declared like the 
following.

{% highlight python %}
# A set
{'a','b','c'}
#A frozenset
frozenset({'a','b','c'}) 
# the argument to frozenset can be any iterable, including a list or tuple
{% endhighlight %}

What is the usefulness of a set? The main advantages of a set are that there
are no duplicates, and that lookups can be done in constant time. For 
example, let's say that you have a very long string of words separated by 
newlines, and you want to find out whether each word in a list of words was 
contained in that string. How would you accomplish this? The first thing 
you might try is.

{% highlight python %}
contained = [(word in long_string) for word in word_list]
{% endhighlight %}

But this is not very efficient, because you have to go searching in the 
string every single time. Now what if we first split the string into a list?

{% highlight python %}
long_string_list = long_string.split()
contained = [(word in long_string_list) for word in word_list]
{% endhighlight %}

This is also not quite so efficient, because looking up an item in a list 
still takes O(n) time. Now, what if we used a set?

{% highlight python %}
long_string_set = set(long_string.split())
contained = [(word in long_string_set) for word in word_list]
{% endhighlight %}

Looking up a word in a set happens in constant time, so this method is very
efficient. Now of course, splitting a string into a list and turning a list 
into a set involve some processing cycles of their own, which is why the 
third way will only be fastest for very large lists. For very small lists, 
the first way is still faster.

## Generators

Python's generators are one of its most powerful features. A generator 
function essentially looks like this.

{% highlight python %}
def generator():
    yield "one"
    yield "two"
    yield "three"
{% endhighlight %}

It can be used like so...

{% highlight python %}
for num in generator():
    print num
{% endhighlight %}

The previous code sample would print the strings "one", "two", and "three".
Each call of the `yield` statement will send another value to the for loop.
Of course, you don't have to use it in a for loop. You could also do...

{% highlight python %}
gen = generator()
next(gen) # "one"
next(gen) # "two"
next(gen) # "three"
next(gen) # Throws 'StopIteration' exception
{% endhighlight %}

You can also send values into the generator. For instance...

{% highlight python %}
def generator():
    x = 0
    while True
        x = yield x+1

gen = generator()
next(gen) # yields 1
gen.send(3) # yields 4
{% endhighlight %}

This allows the generator to function as a coroutine. It's usefulness is 
probably limited, but pretty cool nonetheless.

But the real power of generators is that they allow you to write text 
processing programs that can function in constant memory no matter the size
of the file. How? It's because the file object implements the same interface
as a generator.

{% highlight python %}
for line in open('something.txt'):
    dosomething(line)
{% endhighlight %}

As you can tell, this program will read a file in line by line and do 
something to each line. This way, you could potentially do processing on
Gigabyte-sized files without needing a Gigabyte or so of memory.
