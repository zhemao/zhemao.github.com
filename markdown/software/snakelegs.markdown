Snakelegs: Simplicity by Design

Snakelegs is a Python ORM for MongoDB that follows the KISS ("Keep it Simple,
Stupid") principle.

You may ask what the significance of the name "Snakelegs" is. It is not, as you
may think, because it is written in python. It actually comes from a
Chinese parable about a contest to see who could draw a snake the fastest.
The first contestant to finish drawing finished well before the others, so he
decided to embellish his drawing by drawing legs on the snake. The second
contestant to finish then claimed that he was the first. The first contestant
raised a complaint, but the judge sided with the second contestant, stating,
"Who ever heard of a snake with legs?" Thus arises the Chinese idiom:
"Drawing legs on the snake," meaning, "making things complicated when it is
unneccessary and possibly detrimental." 

I started writing snakelegs after having a bad experience with a different
python Mongo ORM called MongoEngine. MongoEngine tries to abstract the
database querying to use a Django-like syntax. This is sort of silly
because Django's database querying syntax was designed for use with
relational databases, and MongoDB's own query syntax is already simple and 
powerful. I felt that such pointless abstraction was a waste of precious
processing cycles. In Snakelegs, you query MongoDB using the same dict-based
query language that the PyMongo driver uses. Snakelegs simply provides a
Document class with methods that allow you to work with MongoDB in an
intuitive, object-oriented way.

## Dependencies:
[MongoDB](http://mongodb.org) database server with the corresponding python
driver, [PyMongo](http://api.mongodb.org/python/).

## Installation:

Method 1) pip install snakelegs (may need to run as root)

Method 2) Download the latest release from
[here](http://zhehaomao.com/static/files/snakelegs/snakelegs-0.1.2.tar.gz) or clone
my git repo on [github](https://github.com/zhemao/snakelegs). Navigate to
whereever snakelegs was extracted or cloned and run python setup.py install.

## License:
Snakelegs is released under the simplified BSD License, the full text of which 
can be found [here](http://zhehaomao.com/static/bsd-license.txt).

## Getting Help:

A User's Guide is available [here](/blog/software/snakelegs-user-guide).
API Documentation is available at http://packages.python.org/snakelegs/. 

I've tried to make the documentation clear, but if you have any problems with
Snakelegs, please contact me at zhehao.mao@gmail.com. I'd be glad to answer
questions (since that means people are actually using my code).

## Contributing

If you would like to add a feature or fix a bug, feel free to fork the repo and
then send me a pull request. If you would like to get more involved: contact me
and I'll add you as a collaborator.

