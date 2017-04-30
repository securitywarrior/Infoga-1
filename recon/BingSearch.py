#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
#############################################
# Infoga - Email Information Gathering      #
# Coded by Momo Outaadi (M4ll0k) (C) 2017   #
#############################################


from lib import Net
from lib import Printer 
from lib import Parser
import urlparse

class Bingsearch():
	### Bing Search ####
	def __init__(self,Keyword):
		self.Keyword = Keyword
		self.Results = ""

	def UrlCheck(self,url):
		if urlparse.urlsplit(url).netloc == '':
			if urlparse.urlsplit(url).path.startswith("www."):
				return ((urlparse.urlsplit(url).path.split("www.")[1]))
			else:
				return ((urlparse.urlsplit(url).path))
		else:
			if urlparse.urlsplit(url).netloc.startswith("www."):
				return ((urlparse.urlsplit(url).netloc.split("www.")[1]))
			else:
				return ((urlparse.urlsplit(url).netloc))

	def Run(self):
		try:
			((html)) = ((Net.Conn().Httplib("www.bing.com","GET","/search?q=%40"+str(self.UrlCheck(self.Keyword)),"www.bing.com","SRCHHPGUSR=ADLT=DEMOTE&NRSLT=50")))
			if html:
				((self.Results))+=((html)) 
		except Exception,err:
			pass

	def GetEmail(self):
		((FindEmail)) = ((Parser.MyParser(self.Results,self.UrlCheck(self.Keyword))))
		return ((FindEmail.Emails()))

	def Process(self):
		((self.Run()))

