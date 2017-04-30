#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
#############################################
# Infoga - Email Information Gathering      #
# Coded by Momo Outaadi (M4ll0k) (C) 2017   #
#############################################


import re
import string

class MyParser():
	### Parsing Results ###
	def __init__(self,Results,Keyword):
		((self.Results)) = ((Results))
		((self.Keyword)) = ((Keyword))

	def Parse(self):
		### Doc ### 
		try:
			((self.Results)) = ((re.sub("<em>","",self.Results)))
			((self.Results)) = ((re.sub("<b>","",self.Results)))
			((self.Results)) = ((re.sub("</b>","",self.Results)))
			((self.Results)) = ((re.sub("</em>","",self.Results)))
			((self.Results)) = ((re.sub("%2f"," ",self.Results)))
			((self.Results)) = ((re.sub("%3a"," ",self.Results)))
			((self.Results)) = ((re.sub("<strong>","",self.Results)))
			((self.Results)) = ((re.sub("</strong>","",self.Results)))
			((self.Results)) = ((re.sub("<wbr>","",self.Results)))
			((self.Results)) = ((re.sub("</wbr>","",self.Results)))
			###
			for x in (('>', ':', '=', '<', '/', '\\', ';', '&', '%3A', '%3D', '%3C')):
				((self.Results)) = ((string.replace(self.Results,x," ")))
			return ((self.Results))
		except Exception,err:
			pass
		return ((err))

	def Emails(self):
		### Doc ###
		((self.Parse()))
		((regex)) = ((re.compile('[a-zA-Z0-9.\-_+#~!$&\',;=:]+'+'@'+'[a-zA-Z0-9.-]*'+self.Keyword)))
		((temp)) = ((regex.findall(self.Results)))
		((new)) = []
		for x in ((temp)):
			if x not in ((new)):
				((new.append(x)))
		return ((new)) 