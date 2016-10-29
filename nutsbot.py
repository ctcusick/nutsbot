#!/usr/bin/python

import telnetlib, sys, time, os, commands
from xml.dom import minidom   

HOST = 'example.org'
PORT = 8888
MYNAME = 'username'
MYPASS = 'password'

telnet = telnetlib.Telnet(HOST, PORT)
telnet.read_until("name:")
telnet.write(MYNAME + '\n') # username
telnet.read_until("sword:")
telnet.write(MYPASS + '\n')  # password
telnet.read_until("continue:")
telnet.write('\n')         # press enter
telnet.write('\n')
telnet.write('\n')

# examples of things to do:
telnet.write(".bcast broadcasting something \n") # do this
telnet.read_until("Are you sure about this") # wait until you receive this string

# exit
telnet.write('.q\n')
sock.close()
