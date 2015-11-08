#parserDataDump.py

# for pandas
import math
import pandas as pd

# for parsing
from bs4 import BeautifulSoup
import urllib.request

def deDivElement(e):
        '''remove just </div><div> tags'''

        out = e.replace("</div>","")
        
        return out

def deWhiteSpaceElement(e):
        '''strip out the whitepsace in a parsed element'''
        
        out = "".join(line.strip() for line in e.split("\n"))

        return out
        
def runParse():
        '''run parser'''
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
                    #classList.append(url)
                    newDataRow = []
                    urlOpen = urllib.request.urlopen(url)
                    course = subject + " " + cNum
                    newDataRow.append(course)
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

                        newDataRow.append(pText)

                        for element in classText:
                            if "Section" in element:
                                cleanElement = deWhiteSpaceElement(deDivElement(element))
                                newDataRow.append(cleanElement)
                                print(cleanElement)

                            if "Class number" in element:
                                cleanElement = deWhiteSpaceElement(deDivElement(element))
                                newDataRow.append(cleanElement)
                                print(cleanElement)

                            if "Meeting time" in element:
                                cleanElement = deWhiteSpaceElement(deDivElement(element))
                                newDataRow.append(cleanElement)
                                print(cleanElement)

                            if "Location" in element:
                                cleanElement = deWhiteSpaceElement(deDivElement(element))
                                newDataRow.append(cleanElement)
                                print(cleanElement)

                        #this would be instructor when its found
                        #TODO - Instructor

                        #then we append that row to the outer list
                        newDataRow.append("")
                        parsedData.append(newDataRow)
                i = i + 2
        ##########################
        ###############
        # do data parse
        # 1 entry == 1 array
        # for each array, form it as a row
        # for the below line:
        # parsedData.append(row)
        ###############
        return parsedData

# this works

def parsedDataToDataFrame(parsedData):
        '''dumps all rows to data frame'''

        #print(parsedData)
        season = []
        section = []
        classNumber = []
        meetingTime = []
        location = []
        instructor = []

        for row in parsedData:
                season.append(row[0])
                section.append(row[1])
                classNumber.append(row[2])
                meetingTime.append(row[3])
                location.append(row[4])
                instructor.append(row[5])
        #print("{}\n{}\n{}\n{}\n{}\n{}".format(season, section, classNumber, meetingTime, location, instructor))
        parsedDataDataFrame = pd.DataFrame({'Season':season,'Section':section,'Class Number':classNumber,'Meeting Time':meetingTime,'Location':location,'Instructor':instructor})
        parsedDataDataFrame.to_csv('Catalog.csv',index=False,columns=['Major','Season','Section','Class Number','Meeting Time','Location','Instructor'], engine='python')

parsedDataToDataFrame(runParse())
