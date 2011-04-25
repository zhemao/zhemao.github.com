Snakelegs User Guide

## Connecting

Before you can use snakelegs. You will have to open a connection to MongoDB. This can be achieved quite easily with the `connect` function. Just do:

	:::python
	from snakelegs import connect

	connect('mydatabase', 'localhost', 27094, 'username', 'password')

This will connect to the database "mydatabase" on the MongoDB instance
listening on the port 27094 on localhost. It will also authenticate against
the server with credentials "username" and "password" (this is just an example,
do not actually use those credentials). All of these arguments are optional.
The default database is "snakelegs", the default host is "localhost", and the
default port is the default Mongo port: 27017. Username and password are blank
by default. When they are blank, snakelegs will assume that the Mongo instance
is running in a trusted environment (which is the default if you are running it
on your local machine).

## Defining a Document

In Snakelegs, a Model (in the MVC sense) is called a Document. You can
represent your data by creating a subclass of Document like so:

    :::python
    class MyDocument(Document):
        astring = StringField()
        anint = IntField()

That's it. To create a document, just do this:

    :::python
    doc = MyDocument(astring='foo', anint=1)

Then you can save your document with `doc.save()`.

## Finding documents in MongoDB

To query for documents with snakelegs, you can use the `find` method, which is
a classmethod in the Document class. You can use it like so.

    :::python
    docs = MyDocument.find({'astring':'foo'})

This will return a list of instances of MyDocument that match the query. The query syntax is just the PyMongo query syntax. You should consult the PyMongo manual at [[http://api.mongodb.org/python/]] for more.

If you only want a single result instead of a list, you can use the find_one
classmethod.

    :::python
    doc = MyDocument.find_one({'astring':'foo'})

This will return the first document that matches the query.

Deleting a document is as easy as saving one. It's just `doc.delete()`.



