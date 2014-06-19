# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 14:48:18 2014

@author: quicksilver
"""

from bs4 import BeautifulSoup
import urllib2
import os

headers = { 'User-Agent' : 'Mozilla/4.0' }
#url = 'https://www.google.co.in/search?hl=en&authuser=0&site=imghp&tbm=isch&source=hp&biw=1080&bih=756&q=audrey+hepburn&oq=au&gs_l=img.3.0.0l10.1612.4806.0.7247.3.2.1.0.0.0.227.393.0j1j1.2.0....0...1ac.1.42.img..0.3.396.sdj3BEzoce4'
#url = 'http://en.wikipedia.org/wiki/Image'

url = 'https://www.google.co.in/search?site=imghp&tbm=isch&source=hp&biw=1080&bih=756&q=earth&oq=earth&gs_l=img.3..0l10.2687.4177.0.4650.5.5.0.0.0.0.220.788.1j3j1.5.0....0...1ac.1.42.img..1.4.629.7Ek33V4q3jg'
response = urllib2.urlopen(url,str(headers))
html = response.read()
#print str(html)
soup = BeautifulSoup(''.join(html))

images = soup.find_all('img')

#print images

counter = 1
for image in images:
	source = image['src'][2:]
	#os.system('chromium-browser '+ source + '&')
	f = open('image'+ str(counter) + '.jpg','wb' )
	print source +'\n'
	image_response = urllib2.urlopen('http://'+source,str(headers))
	image_file = image_response.read()
	f.write(image_response)
	f.close()
	counter = counter + 1
	