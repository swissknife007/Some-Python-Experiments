import urllib2
import os
counter = 1
headers = str({ 'User-Agent' : 'Mozilla/5.0' })
while counter<=20:
	try:
		url_name = "http://www.glassdoor.com/Reviews/Employee-Review-Adobe-RVW" + str(counter) + ".htm"
		response = urllib2.urlopen(url_name,headers)
		html = response.read()	
		output_file_name = "download"+ str(counter) + ".out";
		output_file = open(output_file_name,'w+')
		output_file.write(html)
		os.system("python gd2.py "+ output_file_name)
		counter = counter + 1
	except urllib2.HTTPError, e:
		counter = counter + 1
	

	
