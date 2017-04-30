#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
#############################################
# Infoga - Email Information Gathering      #
# Coded by Momo Outaadi (M4ll0k) (C) 2017   #
#############################################


import Colors 

class MyInfo():
	### Doc ###
	def CodeName(self):
		###
		return (("%sSkeleton%s"%(Colors.MyColors().red(1),Colors.MyColors().end())))
	def Name(self):
		###
		return (("Infoga"))
	def Vers(self):
		###
		return (("Infoga v4.0"))
	def Disc(self):
		###
		return (("Email Information Gathering"))
	def Author(self):
		###
		return (("%sMomo Outaadi%s (%s@M4ll0k%s)"%(Colors.MyColors().white(4),Colors.MyColors().end(),Colors.MyColors().yellow(1),\
			Colors.MyColors().end())))
	def Git(self):
		###
		return (("%shttps://github.com/m4ll0k/infoga%s"%(Colors.MyColors().yellow(4),Colors.MyColors().end())))