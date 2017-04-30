#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
#############################################
# Infoga - Email Information Gathering      #
# Coded by Momo Outaadi (M4ll0k) (C) 2017   #
#############################################


class MyColors():
	### Doc ### 
	def red(self,num):
		# changing var num return red, normal red, ...
		return (("\033[%d;31m"%(int(num))))
	def end(self):
		# reset colors 
		return (("\033[0m"))
	def white(self,num):
		# return white, normal white, ...
		return (("\033[%d;38m"%(int(num))))
	def green(self,num):
		# return green, normal green
		return (("\033[%d;32m"%(int(num))))
	def yellow(self,num):
		# return  yellow, normal yellow
		return (("\033[%d;33m"%(int(num))))
	def blue(self,num):
		# return blue, normal blue, ...
		return (("\033[%d;34m"%(int(num))))



