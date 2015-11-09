# parserDataDump.py

# for pandas
import pandas as pd

# for parsing
from bs4 import BeautifulSoup
import urllib.request



def deDivElement(e):
    '''remove just </div><div> tags'''

    out = e.replace("</div>", "")
    out = out.replace("<div>", "")

    return out


def deWhiteSpaceElement(e):
    '''strip out the whitepsace in a parsed element'''

    out = "".join(line.strip() for line in e.split("\n"))

    return out

def ampersandCleaner(e):
    '''removes amp; from urls'''

    out = e.replace("amp;","")

    return out

def runParse():
    '''run parser'''

    depaul = "http://www.cdm.depaul.edu"
    parsedData = []
    allMajors = ['animation-animator.txt','animation-ta.txt','BIT.txt','cinema-post.txt','cinema-production.txt',
                 'cinema-sound.txt','cns-governance.txt','cns-networkSecurity.txt','cns-security.txt','comp-finance.txt',
                 'comp-science.txt','e-commerce.txt','game-development.txt','hci.txt','health-informatics.txt',
                 'is-bi.txt','is-bs.txt','is-da.txt','is-enterprise.txt','is-standard.txt','it-project.txt',
                 'media-arts.txt','network-engineering.txt','pa-comp.txt','pa-healthcare.txt','pa-hospitality.txt',
                 'pa-marketing.txt','se-entrepreneurship.txt','se-game.txt','se-project.txt','se-software.txt','se-softwareDev.txt']

    found = set()
    
    for major in allMajors:
        file = open(major, "r")
        print("Opening: {}".format(major))
        line = file.readline()

        courses = line.split('|')
        #print(courses)
        
        for course in courses:
            
            if course in found:
               print("Course already has been parsed: {}".format(course))
               continue

            found.add(course)
            course = course.split(' ')
            
            subject = course[0]
            cNum = course[1]
            
            url = "http://www.cdm.depaul.edu/academics/pages/courseinfo.aspx?Subject=" + \
                subject + "&CatalogNbr=" + cNum
            
            urlOpen = urllib.request.urlopen(url)
            soup = BeautifulSoup(urlOpen, 'html.parser')

            schedule = soup.findAll("div", "schedule")

            # schedule is a Result.Set
            # sched is an element.Tag
            # print(type(schedule))
            for sched in schedule:
                season = sched.find("p", "CTIPageSectionHeader")
                thisSeason = season.getText()
                # append season
                
                
                classInfo = sched.findAll("div", "classInfo")
                #print(type(classInfo))
                for isClass in classInfo:
                    aClass = isClass.findAll("div")

                    # make row. append members as they are found
                    newCourseRow = []
                    
                    newCourseRow.append(subject + " " + cNum)
                    newCourseRow.append(thisSeason)
                    #print(str(aClass))
                    for e in aClass:
                        cleanE = deWhiteSpaceElement(deDivElement(str(e)))
                        # print(type(e))
                        if "Section" in str(e):
                            #print(str(cleanE))
                            newCourseRow.append(cleanE)
                            
                        if "Class number" in str(e):
                            #print(str(cleanE))
                            newCourseRow.append(cleanE)
                            
                        if "Meeting time" in str(e):
                            #print(str(cleanE))
                            newCourseRow.append(cleanE)

                        if "Location" in str(e):
                            #print(str(cleanE))
                            newCourseRow.append(cleanE)

                        if "Instructor" in str(e):
                            # get professor + links - these sometimes are not present
                            # "" if not present
                            try:
                                profName = deWhiteSpaceElement(str(e.find("a").getText()))
                            except AttributeError as err:
                                #print("professor name not found: {}".format(err))
                                profName = ""
                            #print(profName)
                            newCourseRow.append(profName)

                            try:
                                profUrl = depaul + ampersandCleaner(e.find("a").get("href"))
                            except AttributeError as err:
                                #print("professor name not found: {}".format(err))
                                profUrl = ""  
                            #print(profUrl)
                            newCourseRow.append(profUrl)
                            
                            try:
                                syllabusUrl = depaul + deWhiteSpaceElement(ampersandCleaner(e.find("span").find("a").get("href")))
                            except AttributeError as err:
                                #print("professor name not found: {}".format(err))
                                syllabusUrl = ""
                            
                            #print(syllabusUrl)
                            newCourseRow.append(syllabusUrl)
##                    print(newCourseRow)
                    parsedData.append(newCourseRow)
##                    break
                    
                    # append class to data found
                    
##                break
##        break        
        file.close()


    return parsedData




def parsedDataToDataFrame(parsedData):
    '''dumps all rows to data frame'''

    # print(parsedData)
    className = []
    season = []
    section = []
    classNumber = []
    meetingTime = []
    location = []
    instructor = []
    instructorUrl = []
    syllabusUrl = []

    print("there are {} rows in my data".format(len(parsedData)))
    for row in parsedData:
        className.append(row[0])
        season.append(row[1])
        section.append(row[2])
        classNumber.append(row[3])
        meetingTime.append(row[4])
        location.append(row[5])
        instructor.append(row[6])
        instructorUrl.append(row[7])
        syllabusUrl.append(row[8])

    print(instructorUrl)
    parsedDataDataFrame = pd.DataFrame({'Class Name': className,
                                        'Season': season,
                                        'Section': section,
                                        'Class Number': classNumber,
                                        'Meeting Time': meetingTime,
                                        'Location': location,
                                        'Instructor': instructor,
                                        'Insutructor Url': instructorUrl,
                                        'Syllabus Url':syllabusUrl})
    parsedDataDataFrame.to_csv(
        'Catalog.csv',
        index=False,
        columns=['Class Name',
                 'Season',
                 'Section',
                 'Class Number',
                 'Meeting Time',
                 'Location',
                 'Instructor',
                 'Insutructor Url',
                 'Syllabus Url'],
        engine='python')

parsedDataToDataFrame(runParse())
