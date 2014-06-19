#!/usr/bin/env python
import os
from xmpp import Client,Iq,Node
import sys
username = "ajindal121"       
password = "limerenceroger"
domain = "gmail.com"

 

import warnings
warnings.filterwarnings("ignore") 
from xmpp import *
 
cl=Client(server='gmail.com',debug=[])
if not cl.connect(server=('talk.google.com',5222)):
    raise IOError('Can not connect to server.')
if not cl.auth(username, password, domain):
    raise IOError('Can not auth with server.')
cl.send(Iq('set','google:shared-status', payload=[
        Node('show',payload=[sys.argv[1]]),
        Node('status',payload=[sys.argv[2] if len(sys.argv)>2 else ""])
]))
cl.disconnect()
