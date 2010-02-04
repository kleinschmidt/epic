#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import re
import urllib2

#address = 'http://epicurious.com/recipesmenus/global/recipes'
#page = urllib2.urlopen(address)

#source = page.read()

#print(source)

recipeRoot = 'http://www.epicurious.com'
menuSuffix = '/recipesmenus/global/recipes'

#soup = BeautifulSoup(open('/Users/dave/projects/epicurious/recipe_list.html').read())
soup = BeautifulSoup(urllib2.urlopen(recipeRoot + menuSuffix).read())

#for tag in soup.findAll('a',attrs={'class':'recipe_detail_lnk'}):
#    print recipeRoot + tag['href']
    
def getRecipeSoup(url):
    return BeautifulSoup(urllib2.urlopen(url).read())

links = soup.findAll('a',attrs={'class':'recipe_detail_lnk'})
recipeSoups = [getRecipeSoup(recipeRoot + tag['href']) for tag in links]

slPrefix = '/recipes/shoppinglist/custom'
