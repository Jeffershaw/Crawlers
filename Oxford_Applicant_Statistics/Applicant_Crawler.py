# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:43:30 2017

@author: Jeff
"""
#env: python2.7
#unfinished
import urllib2
from lxml import etree

base_url = "https://www.ox.ac.uk"
response = urllib2.urlopen("https://www.ox.ac.uk/admissions/graduate/courses/courses-a-z-listing?combine=&wssl=1")
body = response.read()

page = etree.HTML(body)

result = page.xpath("//div[@class='course-listing clearfix']")
data = {}

for item in result:
    head = item.getchildren()[0]
    mode = item.getchildren()[1].text
    length = item.getchildren()[2].text
    title = head.getchildren()[0]
    department = head.getchildren()[1].text
    title = title.getchildren()[0]
    data[title.text]={'mode':mode,
                    'length':length,
                    'department':department,
                    'url':title.attrib['href']}


#because the data structure is complicate, this crawler is cool cool.