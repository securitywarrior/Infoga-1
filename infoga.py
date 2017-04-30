#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
#############################################
# Infoga - Email Information Gathering      #
# Coded by Momo Outaadi (M4ll0k) (C) 2017   #
#############################################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from lib import Net 
from lib import Parser
from lib import Colors 
from lib import Info 
from lib import Printer 
from lxml.html import fromstring
from recon import *
import json
import os 
import sys
import getopt 
import socket
import re
import urllib3
import urlparse
import requests


class Infoga(object):
	### Infoga Main ###
	def __init__(self,argv):
		self.argv = argv
		self.c = Colors.MyColors()
		self.i =  Info.MyInfo()
		self.AllEmails = []

	def Banner(self):
		print self.c.red(1)+"    __        ___                     "+self.c.end()
		print self.c.red(1)+"   |__.-----.'  _.-----.-----.---.-.  "+self.c.end()
		print self.c.red(1)+"   |  |     |   _|  _  |  _  |  _  |  "+self.c.end()
		print self.c.red(1)+"   |__|__|__|__| |_____|___  |___._|  "+self.c.end()
		print self.c.red(1)+"                       |_____|        "+self.c.end()
		print self.c.white(0)+"--=[ %s - %s                        "%(self.i.Name(),self.i.Disc())+self.c.end()
		print self.c.white(0)+"--=[ %s - \"%s\"                    "%(self.i.Vers(),self.i.CodeName())+self.c.end()
		print self.c.white(0)+"--=[ %s                             "%(self.i.Author())+self.c.end()
		print self.c.white(0)+"--=[ %s                             "%(self.i.Git())+self.c.end()
		print ""

	def Usage(self):
		path = ((os.path.basename(sys.argv[0])))
		self.Banner()
		print "Usage: %s -t [target] -s [source]\n"%(path)
		print "\t-t --target\tDomain to search"
		print "\t-s --source\tData source: [all,google,bing,yahoo,pgp]"
		print "\t-i --info\tGet email informations"
		print "\t--update\tUpdate tool"
		print "\t--version\tShow version"
		print "\t--help\t\tShow this help and exit\n"
		print "Examples:"
		print "\t %s --target site.com --source all"%(path)
		print "\t %s --target site.com --source [google,bing,...]"%(path)
		print "\t %s --info emailtest@site.com"%(path)
		print "";sys.exit()

	def GetInfo(self):
		for x in range(len(self.AllEmails)):
			Printer.MyPrinter().mprint("Email: %s"%(self.AllEmails[x]))
			data = {'lang':'en'}
			data['email'] = self.AllEmails[x]
			req = requests.post("http://mailtester.com/testmail.php",data=data)
			regex = re.compile("[0-9]+(?:\.[0-9]+){3}")
			ip = regex.findall(req.content)
			new = []
			for e in ip:
				if e not in new:
					new.append(e)
			for s in range(len(new)):
				net = urllib3.PoolManager()
				res = net.request("GET","https://api.shodan.io/shodan/host/"+new[s]+"?key=UNmOjxeFS2mPA3kmzm1sZwC0XjaTTksy")
				jso = json.loads(res.data)
				try:
					self.sock = socket.gethostbyaddr(new[s])[0]
				except socket.herror,err:
					try:
						self.sock = jso["hostnames"][0]
					except KeyError,err:
						pass
				if "country_code" and "country_name" in jso:
					print "\t\t|_ %s (%s)"%(new[s],self.sock)
					print "\t\t\t|"
					print "\t\t\t|__ Country: %s(%s) - City: %s (%s)"%(jso["country_code"],jso["country_name"],jso["city"],jso["region_code"])
					print "\t\t\t|__ ASN: %s - ISP: %s"%(jso["asn"],jso["isp"])
					print "\t\t\t|__ Latitude: %s - Longitude: %s"%(jso["latitude"],jso["longitude"])
					print "\t\t\t|__ Hostname: %s - Organization: %s"%(jso["hostnames"][0],jso["org"])
					try:
						print "\t\t\t|__ Vulns: %s - Ports: %s"%(jso["vulns"][0],jso["ports"][0])
					except KeyError,err:
						pass
					print ""
				elif "No information available for that IP." or "error" in jso:
					print "\t\t|_ %s %s"%(new[s],self.sock)
					print "\t\t\t|__ No information available for that IP!!"
					print ""
				else:
					print "\t\t|__ %s (%s)"%(new[s],self.sock)
			sys.exit()

	def Google(self):
		Printer.MyPrinter().nprint("Searching \"%s\" in Google..."%(self.CheckUrl(self.Keyword)))
		Search = GoogleSearch.Googlesearch(self.CheckUrl(self.Keyword))
		Search.Process()
		Emails = Search.GetEmail()
		self.AllEmails.extend(Emails)

	def Bing(self):
		Printer.MyPrinter().nprint("Searching \"%s\" in Bing..."%(self.CheckUrl(self.Keyword)))
		Search = BingSearch.Bingsearch(self.CheckUrl(self.Keyword))
		Search.Process()
		Emails = Search.GetEmail()
		self.AllEmails.extend(Emails)

	def Yahoo(self):
		Printer.MyPrinter().nprint("Searching \"%s\" in Yahoo..."%(self.CheckUrl(self.Keyword)))
		Search = YahooSearch.Yahoosearch(self.CheckUrl(self.Keyword))
		Search.Process()
		Emails = Search.GetEmail()
		self.AllEmails.extend(Emails)

	def Pgp(self):
		Printer.MyPrinter().nprint("Searching \"%s\" in Pgp..."%(self.CheckUrl(self.Keyword)))
		Search = PgpSearch.Pgpsearch(self.CheckUrl(self.Keyword))
		Search.Process()
		Emails = Search.GetEmail()
		self.AllEmails.extend(Emails)

	def All(self):
		self.Google()
		self.Bing()
		self.Yahoo()
		self.Pgp()

	def CheckUrl(self,url):
		o = urlparse.urlsplit(url)
		scheme = o.scheme 
		netloc = o.netloc
		path = o.path
		if scheme not in ["http","https",""]:
			self.Banner()
			sys.exit(Printer.MyPrinter().eprint("Scheme %s not supported!"%(scheme)))
		if netloc == "":
			if path.startswith("www."):
				return path.split("www.")[1]
			else:
				return path
		else:
			if netloc.startswith("www."):
				return netloc.split("www.")[1]
			else:
				return netloc

	def Getinfo(self,email):
		Printer.MyPrinter().mprint("Email: %s"%(email))
		data = {'lang':'en'}
		data['email'] = email
		req = requests.post("http://mailtester.com/testmail.php",data=data)
		regex = re.compile("[0-9]+(?:\.[0-9]+){3}")
		ip = regex.findall(req.content)
		new = []
		for e in ip:
			if e not in new:
				new.append(e)
		for s in range(len(new)):
			net = urllib3.PoolManager()
			res = net.request("GET","https://api.shodan.io/shodan/host/"+new[s]+"?key=UNmOjxeFS2mPA3kmzm1sZwC0XjaTTksy")
			jso = json.loads(res.data)
			try:
				self.sock = socket.gethostbyaddr(new[s])[0]
			except socket.herror,err:
				try:
					self.sock = (jso["hostnames"][0])
				except KeyError,err:
					pass
			if "country_code" and "country_name" in jso:
				print "\t\t|_ %s (%s)"%(new[s],self.sock)
				print "\t\t\t|"
				print "\t\t\t|__ Country: %s(%s) - City: %s (%s)"%(jso["country_code"],jso["country_name"],jso["city"],jso["region_code"])
				print "\t\t\t|__ ASN: %s - ISP: %s"%(jso["asn"],jso["isp"])
				print "\t\t\t|__ Latitude: %s - Longitude: %s"%(jso["latitude"],jso["longitude"])
				print "\t\t\t|__ Hostname: %s - Organization: %s"%(jso["hostnames"][0],jso["org"])
				try:
					print "\t\t\t|__ Vulns: %s - Ports: %s"%(jso["vulns"][0],jso["ports"][0])
				except KeyError,err:
					pass
				print ""
			elif "No information available for that IP." or "error" in jso:
				print "\t\t|_ %s (%s)"%(new[s],self.sock)
				print "\t\t\t|__ No information available for that IP!!"
				print ""
			else:
				print "\t\t|__ %s (%s)"%(new[s],self.sock)
		sys.exit()

	def CheckEmail(self,email):
		if "@" not in email:
			self.Banner()
			sys.exit(Printer.MyPrinter().eprint("Invalid email!! Check your email"))
		self.Banner()
		self.Getinfo(email)

	def CheckVersion(self):
		sys.exit(self.i.Vers())

	def CheckUpdate(self):
		self.Banner()
		if ".git" not in os.listdir(os.getcwd()):
			sys.exit(Printer.MyPrinter().eprint("Git directory not found, please download Infoga from Github repository"))
		elif ".git" in os.listdir(os.getcwd()):
			Printer.MyPrinter().nprint("Updateting...")
			os.chdir(os.getcwd()+"/.git")
			os.system("git pull")
			sys.exit()

	def Start(self):
		if len(sys.argv) < 2:
			self.Usage()
		try:
			opts,args = getopt.getopt(self.argv,"t:s:i:",["target=","source=","info=","update","version","help"])
		except getopt.GetoptError:
			self.Usage()
		for opt,arg in opts:
			if opt in ("-t","--target"):
				self.Keyword = arg
				self.CheckUrl(self.Keyword)
			elif opt in ("-s","--source"):
				self.engine = arg 
				if self.engine not in ("all","google","bing","yahoo","pgp"):
					self.Banner()
					sys.exit(Printer.MyPrinter().eprint("Invalid search engine!! Try with: all,google, bing, yahoo or pgp"))
			elif opt in ("-i","--info"):
				self.email = arg 
				self.CheckEmail(self.email)
			elif opt == "--help":
				self.Usage()
			elif opt == "--version":
				self.CheckVersion()
			elif opt == "--update":
				self.CheckUpdate()

		self.Banner()
		Netcraft.netcraft(self.CheckUrl(self.Keyword)).Run()
		if self.engine == "google":
			self.Google()
		if self.engine == "bing":
			self.Bing()
		if self.engine == "yahoo":
			self.Yahoo()
		if self.engine == "pgp":
			self.Pgp()
		if self.engine == "all":
			self.All()
		if self.AllEmails == []:
			sys.exit(Printer.MyPrinter().eprint("Not found email!"))
		else:
			self.AllEmails = sorted(set(self.AllEmails))
			Printer.MyPrinter().nprint("All email found: ")
			self.GetInfo()

if __name__ == "__main__":
	try:
		Infoga(sys.argv[1:]).Start()
	except KeyboardInterrupt,err:
		sys.exit(Printer.MyPrinter().eprint("Ctr+c...:("))