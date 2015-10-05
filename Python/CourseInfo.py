import unicodedata
import math
import urllib2
from BeautifulSoup import BeautifulSoup

file = open("animation-ta.txt", "w")
page = urllib2.urlopen("http://www.cdm.depaul.edu/academics/Pages/CourseCatalog.aspx")
soup = BeautifulSoup(page)
print soup