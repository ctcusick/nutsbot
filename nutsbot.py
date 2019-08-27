#!/usr/bin/python3

import telnetlib, sys, time, os
from xml.dom import minidom   

HOST = 'example.org'
PORT = 8888
MYNAME = 'username'
MYPASS = 'password'

telnet = telnetlib.Telnet(HOST, PORT)
telnet.read_until(b'name:')
telnet.write((MYNAME + '\n').encode('ascii')) # username
telnet.read_until(b'sword:')
telnet.write((MYPASS + '\n').encode('ascii')) # password
telnet.read_until(b'continue:')
telnet.write(('\n').encode('ascii'))          # press enter
telnet.write(('\n').encode('ascii'))          # press enter
telnet.write(('\n').encode('ascii'))          # press enter

# examples of things to do:
telnet.write((".bcast broadcasting something \n").encode('ascii')) # do this
telnet.read_until(b'Are you sure about this') # wait until you receive this string

# exit
telnet.write(('.q\n').encode('ascii'))
sock.close()
