The Poor Man's Blog Engine: No Database Required

I finally got around to implementing a blog feature on my site. As the title
suggests, the implementation is rather simple. Unlike mainstream blog engines
like Wordpress, which require a database backend and include fancy things like
a WYSIWIG editor, my custom blog engine simply uses the native filesystem.

"But how?" you may ask. "Good question" I say. The way it works is that each
article is in fact a Markdown file sitting in a directory on the server.
The url of the article is just the filename. The first line in the file is used as the article
title, and everything else is used as the article body. The date created and the date modified
are taken by simply performing a `stat` command (actually, by using the `os.stat`
function in the Python stdlib, but it's basically the same thing). The article
body is passed through the python [Markdown](http://www.freewisdom.org/projects/python-markdown/)
module, and the article itself goes through web.py to jinja2 and then out to the browser.
To create an article, I just make a new markdown file. And to edit, I just use
a regular text editor.

Your next question, *hopefully*, may be "That sounds cool, can I use it?" The answer is
that the engine is not really standalone just yet. If there is any interest,
I may reimplement the engine as a static site generator, in the vein of
[Jekyll](https://github.com/mojombo/jekyll) and [Hyde](http://ringce.com/hyde).
I suggest looking into either of those two first, as they already exist.




