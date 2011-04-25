Network Hijinks with Netcat

Just recently, I discovered how to use netcat, also known as `nc`, the TCP/IP 
swiss army knife. Netcat can send and receive raw TCP and UDP data. 
In case you don't know, TCP and UDP are the two main ways of sending data over 
the internet. TCP is the more common one, and is the basis of such protocols as 
HTTP, FTP, SSH and much, much more.

Because nc can send and receive raw TCP and UDP packets, it is very flexible and 
can do just about anything. Here are some fun things you can do.

## Sending IMs
In a terminal, type `nc -l 2431`. The `-l` flag tells nc to listen on a port. 
The next argument is the port. In this example, it is 2431. In another terminal, 
type `nc localhost 2431 `. This will tell nc to connect to localhost on port 
2431. Then, whatever you type into one terminal will be output onto the other 
terminal. You are not restricted to localhost, of course. If you tell a friend 
your IP address and have him or her run `nc your-ip your-port` on his or her 
computer, you can send funny messages to each other over the internet.

## Browsing the web
The nc program can also be used to send HTTP requests. For instance, if you type 
`nc www.google.com 80` and then type "GET / HTTP/1.1" followed by 
"Host: www.google.com", Google's webservers will respond with the html for their 
front page.

## HTTP Server
If you run `nc -l 8000` and then navigate with your web browser to 
[http://localhost:8000](http://localhost:8000), You will see HTTP requests from 
the browser on your terminal. If you then type something in nc and close
the connection (by pressing Ctrl+D), you will see the text you typed appear in 
your browser. For some reason, you are not allowed to provide the HTTP headers, 
only the body. Netcat automatically sends "Content-Type: text/plain". Notice 
that this method can only handle one connection, and the program must be 
closed in order to actually send the HTTP response.

## Remote shell
Another funny thing you can do is to implement a remote shell program using 
unix pipes. If you type `nc -l 1234|bash|nc -l 1235` and then open up two other 
terminals and connect one to port 1234 and the other to 1235, you can send shell 
commands to port 1234 and the results of the command will show up on port 1235.
This is horribly insecure, so please don't do this other than for novelty. 
You can do this with other interactive shells as well, such as `sh`, `python`, 
`irb`, etc.

## File transfer
Say you want to send a file to a friend but don't want to bother with opening up 
your email client or web browser, attaching the file to an email and then 
sending it, you can use nc to easily transfer from one computer to another. 
The recipient should run on his computer `nc -l 1838 > something.file`, 
choosing whatever port number and filename they want. The sender should run on 
his computer `nc <recipient's ip> 1838 < something.file`, where something.file 
is the file they wish to transfer. This can work either way, so the sender can 
do the listen and the recipient can do the connect. nc makes
no distinction between client and server once the connection is made.
