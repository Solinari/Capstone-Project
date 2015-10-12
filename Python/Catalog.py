from bs4 import BeautifulSoup
import urllib.request

file = open("BIT.txt", "r") #file of  class required for degree. Can change to whatever we need
line = file.readline()
str = line.replace('|',' ')
list1 = str.split(' ')
print (list1)
i = 0
while i < len(list1):
  subject = list1[i]
  cNum = list1[i + 1]
  url = "http://www.cdm.depaul.edu/academics/pages/courseinfo.aspx?Subject=" + subject + "&CatalogNbr=" + cNum
  print(url)
  # need to save in a list
  i = i + 2