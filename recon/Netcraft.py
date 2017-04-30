#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
#############################################
# Infoga - Email Information Gathering      #
# Coded by Momo Outaadi (M4ll0k) (C) 2017   #
#############################################


from lib import Net 
from lib import Printer 
import re

class netcraft():
	### Netcraft ###
	def __init__(self,target):
		((self.target)) = ((target))
		((self.headers)) = (({'User-agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"}))

	def Run(self):
		try:
			((url)) = (("http://searchdns.netcraft.com/?restriction=site+contains&host=%s&lookup=wait..&position=limited"%(self.target)))
			((html)) = ((Net.Conn().Urllib2(url,None,self.headers)))
			if html:
				((reg)) = ((re.findall('url=\S+"',html,re.I)))
				print ""
				((Printer.MyPrinter().nprint("Searching \""+(self.target)+"\" Websites Correlation...")))
				if reg:
					((Printer.MyPrinter().nprint("Found %s sites "%(len(reg)))))
					print ""
					for x in range(len(reg)):
						((host)) = ((reg[x].split('"')[0]))
						print ((" - %s"%(host.split("url=")[1])))
					print ""
				else:
					((Printer.MyPrinter().iprint("Not found sites")))
		except Exception,err:
			pass
