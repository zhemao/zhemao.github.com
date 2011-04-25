#!/usr/bin/env python

import jinja2 as jj2
import sys, os
from article import Article
from os.path import isfile, isdir

env = jj2.Environment(loader=jj2.FileSystemLoader('templates'),
							autoescape=True)

mdpath = 'markdown/'

def render_template(tmplname, **kwargs):
	template = env.get_template(tmplname)
	return template.render(**kwargs)

def create_list(path, cssprefix):
	names = os.listdir(path)
	articles = []
	for name in names:
		ind = name.rfind('.')
		if name[ind+1:] == 'markdown':
			filepath = path+name
			url = name[:ind]+'.html'
			art = Article(filepath, url)
			articles.append(art)
	if path and isfile(path+'title.txt'):
		title = open(path+'title.txt').read()
	else: title = 'Title'
	articles.sort(key = lambda art: art.modified, reverse=True)
	return render_template('list.html', articles=articles, title=title, cssprefix=cssprefix)
	
def create_article(page, cssprefix):
	filename = mdpath+page
	if isfile(filename):
		article = Article(filename, page)
		return render_template('article.html', article=article, cssprefix=cssprefix)
	raise Exception(filename+' does not exist')

def walk_directory(root, extra=''):
	path = root+'/'+extra
	levels = len(extra.split('/'))
	cssprefix = '../'*levels
	if not isdir('blog/'+extra):
		os.makedirs('blog/'+extra)
	f = open(os.getcwd()+'/blog/'+extra+'index.html', 'w')
	lstr = create_list(root+'/'+extra+'/', cssprefix)
	f.write(lstr)
	f.close()
	for name in os.listdir(path):
		if isdir(path+name):
			walk_directory(root, extra+name+'/')
		elif isfile(path+'/'+name):
			ind = name.rfind('.')
			if ind>0 and name[ind+1:]=='markdown':
				art = create_article(extra+name, cssprefix)
				f = open(os.getcwd()+'/blog/'+extra+'/'+name[:ind]+'.html', 'w')
				f.write(art)
				f.close()

if __name__ == '__main__':
	walk_directory('markdown', '')

