#!/usr/bin/env python3

from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

# simple python3 server to demo website

if __name__=='__main__':
    port = len(sys.argv)>1 and int(sys.argv[1]) or 8000
    httpd = HTTPServer(("",port), SimpleHTTPRequestHandler)
    print("Server running on port "+str(port))
    httpd.serve_forever()
