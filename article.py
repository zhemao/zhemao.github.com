from datetime import date
import os
from markdown import markdown

class Article:
	def __init__(self, filepath, url):
		self.filepath = filepath
		self.url = url
		self.readfile()
		self.gettimeinfo()

	def readfile(self):
		f = open(self.filepath)
		self.title = f.readline().rstrip()
		self.source = f.read()
		self.body = markdown(self.source, ['extra', 'codehilite'])
		

	def gettimeinfo(self):
		stat = os.stat(self.filepath)
		self.created = date.fromtimestamp(stat.st_ctime)
		self.modified = date.fromtimestamp(stat.st_mtime)
