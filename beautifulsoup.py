#!/usr/bin/python
#-*- encoding: utf-8 -*-

import urllib
import BeautifulSoup
import json

url = "http://www.tumblr.com/tagged/猫"

soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(url).read())

for detailsrc in soup.findAll("div", {"class":"stage"}):
    for timesrc in detailsrc.findAll("img"):
        print timesrc['src']
