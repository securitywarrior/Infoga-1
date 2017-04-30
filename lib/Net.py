#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
#############################################
# Infoga - Email Information Gathering      #
# Coded by Momo Outaadi (M4ll0k) (C) 2017   #
#############################################

import httplib
import urllib 
import urllib2
import requests

class Conn():
	###
	def Httplib(self,server,method,query,host,cookie):
		try:
			http = httplib.HTTP(server)
			http.putrequest(method,query)
			http.putheader("Host",host)
			http.putheader("Cookie",cookie)
			http.putheader("Accept-Languagge","en-us,en")
			http.putheader("User-agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1")
			http.endheaders()
			# 
			returncode,returnmsg,headers = http.getreply()
			html = http.getfile().read()
			return html
		except Exception,err:
			pass 
		return err

	def Requests(self,url):
		try:
			req = requests.get(url)
			return req.content
		except Exception,err:
			pass
		return err 

	def Urllib2(self,url,none,headers):
		try:
			req = urllib2.Request(url,none,headers)
			html = urllib2.urlopen(req).read()
			return html
		except Exception,err:
			pass
		return err

