#!/usr/bin/env python
import os
import re

process_list = " " 
process_list_copy = process_list
separator = 'abhishek'
needle = '/usr/bin/vlc'
def get_song(idx1 ):
	#print idx1
	if(idx1 == -1):
		print ('No vlc song being played at the moment ,brother' + '\n')
	else :
		start_idx = idx1 + len(needle)
		#print "start :  " + process_list[start_idx:]+'\n\n\n'
		process_line = process_list[start_idx:]
		#print process_line
		
		end_idx = process_line.find(separator)
		
		song_name = process_list[start_idx : start_idx + end_idx]
		print str(song_name)
		#print ('Song being played ... '+ song_name )


pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

for pid in pids:
    try:
        process_list = process_list + separator + open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
    except IOError: 
        continue
    #print process_list
#print process_list
process_list = process_list + separator
process_list_copy = process_list 
process_list = process_list_copy
occurs_list = [occurs.start() for occurs in re.finditer(needle,process_list )]

#print occurs_list

#print occurs_list
for occur in occurs_list:
	get_song(occur)