---
title: Largest Subarray Problem
layout: post
---

# Solution to the Largest Subarray Problem

Today I was studying some CS Interview Questions in preparation for an on-site
interview. I came across one question which was particularly interesting. 

The question, taken from http://kundansingh.com/interview/#q11 is 

"Given an array containing positive and negative integers, find the subarray
with the largest sum in O(N) time".

The way I started thinking about it is that a subarray of a vector is the
original vector with a certain number of elements lopped off either side.
The lopped off portions each have a sum. How do you maximize the sum of the 
subarray? Clearly by minimizing the sums of the lopped off portions. So, 
basically, you find the indices at which the sum is a minimum going in both
directions, and the subarray you return is bracketed by those two indices 
(exclusive). So, take, for instance, the array 

<table>
<tr><td>1</td><td>-3</td><td>5</td><td>1</td><td>-2</td></tr>
</table>

If you take the sums from either side.

<table>
<tr><th>Index</th><td>-</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>-</td></tr>
<tr><th>Values</th><td>-</td><td>1</td><td>-3</td><td>5</td><td>1</td><td>-2</td><td>-</td></tr>
<tr><th>Leftward Sums</th><td>0</td><td>1</td><td>-2</td><td>3</td><td>4</td><td>2</td><td>-</td></tr>
<tr><th>Rightward Sums</th><td>-</td><td>2</td><td>1</td><td>4</td><td>-1</td><td>-2</td><td>0</td></tr>
</table>

There are hyphens on the left and right because summations begin from 0 on 
either side. We can very well imagine an array where the subarray with the 
largest subarray is the array itself. For instance, this would be true if all
elements were positive. So, if we were to follow the algorithm of minimizing
the pieces chopped off either end. We would clearly return the subarray
from 2 to 3 inclusive. In other words, the subarray containing the 
values 5 and 1. You can pretty easily convince yourself that this is, in fact
the largest subarray. 

There is a special case this algorithm doesn't consider though. What if the 
inclusive left bound is greater than the inclusive right bound? For example,
the array

<table>
<tr><td>-2</td><td>-1</td><td>-2</td><td>3</td><td>1</td></tr>
</table>

In this case, using our current algorithm, we will get the inclusive left bound
to be 3 and the inclusive right bound to be 0. This is, of course, incorrect.
So what is the actual answer? The actual answer is that we keep one of the 
bounds at the calculated value, but either the left bound must be set to 0 or
the right bound must be set to N-1. In this case, it is the latter. We make
the decision based on whether the minimum leftward sum is smaller than the 
minimum rightward sum. Since in this case, the leftward sum is smaller, we keep
the left boundary and set the right boundary to N-1. If it was the other way
around (e.g. the last array reversed), we would keep the right bound
and set the left bound to 0. 

So here is my C code to implement the solution. It takes the number in as 
command-line arguments, and prints out the result in the format of

left bound - right bound : sum

<script src="https://gist.github.com/1384147.js"> </script>
