#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
#############################################
# Infoga - Email Information Gathering      #
# Coded by Momo Outaadi (M4ll0k) (C) 2017   #
#############################################


import Colors
import time 

class MyPrinter():
	### Docs ###
	def __init__(self):
		self.tm = (("%s[%s]%s"%((Colors.MyColors().white(1),time.strftime("%H:%M:%S"),Colors.MyColors().end()))))

	def nprint(self,string,flag="+"):
		print ((self.tm+"%s["%(Colors.MyColors().green(1))+str(flag)+"]%s %s"%(Colors.MyColors().end(),Colors.MyColors().white(0))+str(string)+Colors.MyColors().end()))
	
	def eprint(self,string,flag="!"):
		print ((self.tm+"%s["%(Colors.MyColors().red(1))+str(flag)+"]%s %s"%(Colors.MyColors().end(),Colors.MyColors().white(0))+str(string)+Colors.MyColors().end()))
	
	def iprint(self,string,flag="i"):
		print ((self.tm+"%s["%(Colors.MyColors().yellow(1))+str(flag)+"]%s %s"%(Colors.MyColors().end(),Colors.MyColors().white(0))+str(string)+Colors.MyColors().end()))

	def mprint(self,string,flag="E"):
		print ((self.tm+"%s["%(Colors.MyColors().green(1))+str(flag)+"]%s %s"%(Colors.MyColors().end(),Colors.MyColors().white(0))+str(string)+Colors.MyColors().end()))

