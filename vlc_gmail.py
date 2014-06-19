#!/usr/bin/env python
import os

def process_status(status):
	length = len(status)
	t = '~'
	for char in status:
		if not(char.isdigit()) and not(char.isalpha()):
			continue
		if char ==' ':
			t = t + ''
		elif char == '.':
			continue

		elif char=='/':
			t = t + '//' 
		else:
			t = t + char
	print t
	return t
	"""
def pre2(status):
	status = status.replace('/','//')
	"""
counter = 1;
while 1:
	status = os.popen('python process_list.py').read()
	#print status
	status = process_status(status)
	#print status
	gmail_command = "python gmail_status.py default "
	#os.system(gmail_command + process_status(status))
#os.system("echo "+ '//home//quicksilver//Music//EminemftAkon-SmackThatmp3');
	if counter%10000000000==0 :
		os.system(gmail_command + status)
	counter = counter + 1