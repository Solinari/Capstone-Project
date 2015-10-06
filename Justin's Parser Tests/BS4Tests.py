from bs4 import BeautifulSoup
import urllib.request

# these will all be encapsulated in functions eventually

url = "http://www.cdm.depaul.edu/academics/Pages/MastersDegrees.aspx"
fronturl = "http://www.cdm.depaul.edu"

# function 1 - get the degree links
def findDegreeLinks(url):
    '''finds degree links from  url passed on DePaul's page'''
    myDegreeLinks = []
    urlOpen = urllib.request.urlopen(url)
    soup = BeautifulSoup(urlOpen, 'html.parser')

    # get all the program url's and append them 
    test1 = soup.find_all("p", "programIndexHeader")
    #print(len(test1))

    for i in test1:
        myDegreeLinks.append(str(i).split(' ')[3].split('\"')[1])

    return myDegreeLinks

# end function 1

#function 2 - map concentration links
def findDegreeConcentrations(myDegreeLinks, myFrontUrl):
    '''Find concentrations in degrees'''
    myDegreesAndConcentrations = []
    for degree in myDegreeLinks:
        concentrationLink = myFrontUrl + degree
        #print(concentrationLink)
        outputSize = len(myDegreesAndConcentrations)
        

        # find if concentrations are present
        # append them if found
        urlOpen2 = urllib.request.urlopen(concentrationLink)

        soup2 = BeautifulSoup(urlOpen2, 'html.parser')

        test2 = soup2.find_all("h2", "moduletitle")

        for i in test2:
            sample = str(i).split("\"")
            #print(sample)

            

            for element in sample:
                
                 if "/academics/Pages" in element:
                     #print(element)
                     if fronturl not in element:
                         element = fronturl + element
                         
                     myDegreesAndConcentrations.append(element)

        # if you didn't find anything in the concentrations
        # append that degree url
        if outputSize == len(myDegreesAndConcentrations):
            myDegreesAndConcentrations.append(concentrationLink)


    #all degrees with their concentrations
    print(len(myDegreesAndConcentrations))
    for degree in myDegreesAndConcentrations:
        print(degree)

    return myDegreesAndConcentrations

# end function 2
degreeLinks = findDegreeLinks(url)
degreesAndConcentrations = findDegreeConcentrations(degreeLinks, fronturl)
print(degreesAndConcentrations)










