#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import re,urllib2, sys

VERBOSE = True

infile = open(sys.argvp[1],'r')
out = open(sys.argv[2],'w')

siteroot = 'http://www.epicurious.com'
root = 'http://www.epicurious.com/recipesmenus/global/recipes'

def getsoup(url):
    return BeautifulSoup(urllib2.urlopen(url).read())

for i in range(1,6):
	if VERBOSE: print 'page',i,'('+str(n)+' recipes)'
	opts = '?pageNumber='+str(i)+'&pageSize='+str(n)+'&resultOffset='+str(n*(i-1)+1)
	soup = getsoup(root+opts)
	links = soup.findAll('a',attrs={'class':'recipe_detail_lnk'}) 
	for tag in links:
		out.write(siteroot+tag['href']+'\n')
		#if VERBOSE: print siteroot+tag['href']

infile.close()
out.close()
