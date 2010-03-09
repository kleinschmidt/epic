#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import re,urllib2, sys

VERBOSE = True

out = open(sys.argv[1],'w')

siteroot = 'http://www.epicurious.com'
root = 'http://www.epicurious.com/recipesmenus/global/recipes'
n = 1000	# how many recipes to fetch per page
total = 5000	# total number of recipes

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

out.close()
