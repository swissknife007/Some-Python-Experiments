from  robobrowser import RoboBrowser;
from bs4 import BeautifulSoup;
import robobrowser.helpers;
import json;
import sys;
"""
Take HTML file as input
return Summary,Employer,Employer,Location,Occupation,Pros,Cons etc

"""

def pre_process(soup):
	if soup == None or soup == []:
		return ''
	#print soup;
	if isinstance(soup,list):
	   return ''
	s = soup.encode('utf-8')
	#print(s);
	l = len(s)
	t = ''
	i = 0
	while(i < l):
		#print t;
		if(s[i] == '<'):
			if(i + 4 <= l):
				if(s[i+1]=='b' and s[i+2]=='r' and s[i+3]=='/' and s[i+4]=='>'):
					t = t + ' '
					i = i + 5
					continue
				
			j = i + 1
			while(j < l and s[j] != '>'):
				j = j + 1
			i = j + 1
		else :
			t = t + s[i] 
			i = i + 1
	return t





file_name = sys.argv[1]   
input_html = open(file_name+ '.html','rb+').read()

soup = BeautifulSoup(''.join(input_html))
#print soup;
if soup == None:
	print "None"

output_file = open(file_name+".txt",'w+');
output = 'Title:'+ pre_process(soup.find('div',class_="title"))+'\n'	
output_file.write((output))
output = 'Time Limit:'+ pre_process(soup.find('div',class_="time-limit"))+'\n'
output_file.write((output))
output = 'Memory Limit:'+ pre_process(soup.find('div',class_="memory-limit"))+'\n'	
output_file.write((output))

output = 'Inputs:'+ pre_process(soup.find('div',class_="input-specification"))[5:]+'\n'	
output_file.write((output))
output = 'Outputs:'+ pre_process(soup.find('div',class_="output-specification"))[6:]+'\n'	
output_file.write((output))

#output = 'Sample Tests:\n' #+ pre_process(soup.find('div',class_="sample-tests"))+'\n'

#output_file.write((output))

sub_soup = soup.find('div',class_="sample-test")
#print sub_soup
if sub_soup == None :
	raise Exception
output_inputs = sub_soup.find_all('div',class_="input")	
output_outputs = sub_soup.find_all('div',class_="output")	
input_iter = iter(output_inputs)
output_iter = iter(output_outputs)
for input in output_inputs:
	inp = pre_process(input_iter.next())[6:]
	out = pre_process(output_iter.next())[6:]
	output_file.write("Input " +  inp + '\n')
	output_file.write("Output " + out + '\n')

#print soup;
