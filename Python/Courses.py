import unicodedata
import math
import urllib2
from BeautifulSoup import BeautifulSoup

file = open("se-softwareDev.txt", "w")
page = urllib2.urlopen("http://www.cdm.depaul.edu/academics/Pages/Current/Requirements-MS-SE-Software-Development.aspx")
soup = BeautifulSoup(page)
tables = soup.findAll( "table", {"class":"courseList"} )
for table in tables:
	spans = table.findAll("span", {"class":"CDMExtendedCourseInfo"})
	for span in spans:
		text2 = span.renderContents()
		trimmed_text2 = text2.strip()
		file.write(trimmed_text2)
		file.write("|")
	for row in table:
		cells = row.findAll("td", {"class":"CDMExtendedCourseInfo"})
	   	for cell in cells:
	   		text = cell.renderContents()
	   		trimmed_text = text.strip()
	   		file.write(trimmed_text)
	   		file.write("|")
file.close()