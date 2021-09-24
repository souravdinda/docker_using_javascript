#!/usr/bin/python3

import cgi
import subprocess

print("context-type: text/html")
print()


f = cgi.FieldStorage()
cmd = f.getvalue("x")
#cmd= "kubectl get pods"
a = "sudo "  +  cmd + "   --kubeconfig admin.conf" 
#print(a)
output = subprocess.getoutput(a)
print(output)



# hello testing 
