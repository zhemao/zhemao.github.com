#!/usr/bin/env python2

import jinja2 as j2
import markdown 
import os

md = markdown.Markdown(extensions=['codehilite'], safe_mode=True)
env = j2.Environment(loader=j2.FileSystemLoader('./templates'))
MDPATH='./markdown'

def generate(name):
	f = open(MDPATH+'/'+name, 'r') 
	src = f.read()
	f.close()
	html = md.convert(src)
	ind = name.rfind('.')
	f = open('./'+name[:ind]+'.html', 'w')
	tmpl = env.get_template('base.html')
	f.write(tmpl.render(content=html))
	f.close()
	
if __name__=='__main__':
	for name in os.listdir(MDPATH):
		if name.endswith('.md') or name.endswith('.markdown'):
			generate(name)
	
