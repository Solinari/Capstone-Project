from bs4 import BeautifulSoup
import urllib.request


url = "http://www.cdm.depaul.edu/academics/Pages/MastersDegrees.aspx"

fronturl = "http://www.cdm.depaul.edu"
degreeLinks = []
degreesAndConcentrations = []


urlOpen = urllib.request.urlopen(url)
soup = BeautifulSoup(urlOpen, 'html.parser')

# get all the program url's and append them 
test1 = soup.find_all("p", "programIndexHeader")
#print(len(test1))

for i in test1:
    degreeLinks.append(str(i).split(' ')[3].split('\"')[1])

#print(degreeLinks)
Concentrations = []
for degree in degreeLinks:
    concentrationLink = fronturl + degree
    #print(concentrationLink)
    degreesAndConcentrations.append(concentrationLink)

    # find if concentratinos are present
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
                     
                 degreesAndConcentrations.append(element)


#all degrees with their concentrations
print(len(degreesAndConcentrations))
for degree in degreesAndConcentrations:
    print(degree)

