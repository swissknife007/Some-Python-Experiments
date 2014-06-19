from urllib import request,error
import os
counter = 0
contest_id = 417
char_map = ['A','B','C','D','E']
headers = str({ 'User-Agent' : 'Mozilla/5.0' })
while counter< 5:
	try:
		url_name = "http://www.codeforces.com/problemset/problem/" + str(contest_id) +'/' + char_map[counter]
	#	print url_name
		response = request.urlopen(url_name,headers.encode('utf-8'))
		html = response.read()	
		partial_file_name = str(contest_id)+ '_' + char_map[counter] 
		output_file_name = partial_file_name + ".html"
		output_file = open(partial_file_name + ".html" ,'wb+')
		output_file.write(html);
		os.system("python cf_parse.py " + partial_file_name )
		counter = counter + 1
	except error.HTTPError:
		counter = counter + 1
	

	
