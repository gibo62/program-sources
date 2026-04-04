#!/usr/bin/python
import cgi
print "Content-type: text/html" 
print 
print "<HTML><HEAD></HEAD><BODY>" 
f = open('../funzione.txt')
content = f.read()
f.close
print content
print "</BODY></HTML>"	


