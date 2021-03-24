#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os, time, sys
print '\x1b[1;32m'
from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Enter Site Name \n(ex : example.com or www.example.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link
x = '_____________=︻╦╤─ WELCOME TO MAY SCRIPT RAYANE GRAICHI ─╤╦︻=_______________\nTHIS SECRIPT FISHING \nDATE:2021/3/16\nNAME:Alhamwi \n my insta : al0hamwi \n'
for i in x:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.06)
    animation = '|/-\\'
for i in range(60):
    time.sleep(0.1)
    sys.stdout.write('\r\x1b[32;1m[\x1b[37;1m+\x1b[32;1m]\x1b[37;1m LOADING.\x1b[32;1m' + animation[(i % len(animation))])
    sys.stdout.flush()

print ' '

def Credit():
	Space(9); print "#####################################"
	Space(9); print "#   +++ Admin Panel Finder v1 +++   #"
	Space(9); print "#     Script by Illûmïnåté Ðëmøñ    #"
	Space(9); print "#    Bangladesh Black Hat Hackers   #"
	Space(9); print "#####################################"

Credit()
findAdmin()
