#parserDataDump.py

# for pandas
import math
import pandas as pd

# for parsing
from bs4 import BeautifulSoup
import urllib.request


def runParse():
        '''run the fucking god damn parser'''
        parsedData =[]



        ##########################
        classList = []
        # list = ['animation-animator.txt','animation-ta.txt','BIT.txt','cinema-post.txt','cinema-production.txt',
        #     'cinema-sound.txt','cns-governance.txt','cns-networkSecurity.txt','cns-security.txt','comp-finance.txt',
        #     'comp-science.txt','e-commerce.txt','game-development.txt','hci.txt','health-informatics.txt',
        #     'is-bi.txt','is-bs.txt','is-da.txt','is-enterprise.txt','is-standard.txt','it-project.txt',
        #     'media-arts.txt','network-engineering.txt','pa-comp.txt','pa-healthcare.txt','pa-hospitality.txt',
        #     'pa-marketing.txt','se-entrepreneurship.txt','se-game.txt','se-project.txt','se-software.txt','se-softwareDev.txt']
        # for item in list:
        file = open('BIT.txt', "r") #file of  class required for degree. Can change to whatever we need
        line = file.readline()
        string = line.replace('|',' ')
        list1 = string.split(' ')

        i = 0
        while i < len(list1):
                subject = list1[i]
                cNum = list1[i + 1]
                url = "http://www.cdm.depaul.edu/academics/pages/courseinfo.aspx?Subject=" + subject + "&CatalogNbr=" + cNum
                test = url in classList
                if test == False:
                        classList.append(url)
                i = i + 2

        print (classList[0])
        urlOpen = urllib.request.urlopen(classList[0])
        soup = BeautifulSoup(urlOpen,'html.parser')
        header = soup.find("h2","CDMPageTitle")
        text = header.getText()
        divs = soup.find("div","schedule")
        classInfo = soup.find_all("div","classInfo")
        for info in classInfo:
        #for item in divs:
                term = soup.find("p","CTIPageSectionHeader")
                pText = term.getText()
                print(pText)
                classText = str(info).split("<div>")

                newDataRow = []
                
                newDataRow.append(pText)

                for element in classText:
                        if "Section" in element:
                                elementwodiv = element.replace("</div>","")
                                newDataRow.append(elementwodiv)
                                print(element.replace("</div>",""))
                                                        
                        if "Class number" in element:
                                elementwodiv = element.replace("</div>","")
                                newDataRow.append(elementwodiv)
                                print(element.replace("</div>",""))
                                
                        if "Meeting time" in element:
                                elementwodiv = element.replace("</div>","")
                                newDataRow.append(elementwodiv)
                                print(element.replace("</div>",""))
                                
                        if "Location" in element:
                                elementwodiv = element.replace("</div>","")
                                newDataRow.append(elementwodiv)
                                print(element.replace("</div>",""))

                #this would be instructor when its found
                #TODO - Instructor

                #then we append that row to the outer list
                newDataRow.append("")
                parsedData.append(newDataRow)
        ##########################
        ###############
        # do data parse
        # 1 entry == 1 array
        # for each array, form it as a row
        # for the below line:
        # parsedData.append(row)
        ###############

        return parsedData


def parsedDataToDataframe(parsedData):
	'''dump all rows in data to dataframe'''

	#all fields should be strings***

	# we have 7 data fields per row

	# append this either as a link url or a defined constant
	major = []

	# ie Winter 2015-2016
	season = []

	# course section
	section = []

	# Class ID Number
	classNumber = []

	# Meeting Time
	meetingTime = []

	# Room name/number & Campus
	location = []

	# Instructor - Issue parsing Instructor in parse just enter empter string for this row
	instructor = []


	# so the way this works, we are going to do a Matrix Inversion
	# don't worry about the math, its just turning the table "on its side"
	# for data storage reasons
	# See how for each row I take an element and append it to these new fields?
	for row in parsedData:
                print("row is {} long".format(len(row)))
                print(row)
                major.append(row[0])
                season.append(row[1])
                section.append(row[2])
                classNumber.append(row[3])
                meetingTime.append(row[4])
                location.append(row[5])
                instructor.append(row[6])


	# This is why it matters the order as well as 

	parsedDataDataFrame = pd.DataFrame({'Major' : major,
										'Season' : season,
										'Section' : section,
										'Class Number' : classNumber,
										'Meeting Time' : meetingTime,
										'Location' : location,
										'Instructor' : instructor})

	parsedDataDataFrame.to_csv('Catalog.csv',
								index=False,
								columns=['Major', 'Season', 'Section',
								'Class Number', 'Meeting Time',
								'Location', 'Instructor'],
								engine='python')

parsedDataToDataframe(runParse())
