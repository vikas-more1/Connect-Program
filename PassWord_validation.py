// Language: Python3.7
// Program to vadidate password field with certain rules.
// Rule  1. Password should be atleast 6 characters.
// Rule  2. It must contain atleast a lowercase character , a uppercase character , a digit and a special symbol [ $,@,# ].
// Name : Vikas More.
// College : FERGUSON COLLEGE ( AUTONOMOUS ), FC ROAD, PUNE.
// Department  of Computer Scienece ( PG )

import re

print("Password should be atleat 6 to 16 characters.\nIt should contain atleast 1 UPPERCASE.\nIt should contain atleast 1 lowercase.\nIt should contain atleast 1 special character.\nIt should contain atleast 1 numerical value")
p=input("Input your pasword:-")
x=True
while x:
	if (len(p)<6 and len(p)>16):
		break
	elif not re.search("[a-z]",p):
		break
	elif not re.search("[A-Z]",p):
		break
	elif not re.search("[0-9]",p):
		break
	elif not re.search("[$#@]",p):
		break
	elif re.search("\s",p):
		break
	else:
		print("Valid Password")
		x=False
		break
if x:
