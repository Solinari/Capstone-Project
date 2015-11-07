from bs4 import BeautifulSoup
import urllib.request

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
    # class text is a list
    #print("Class text is: {}".format(classText))
    for element in classText:
        if "Section" in element:
            print(element.replace("</div>",""))
        if "Class number" in element:
            print(element.replace("</div>",""))
        if "Meeting time" in element:
            print(element.replace("</div>",""))
        if "Location" in element:
            print(element.replace("</div>",""))
    #print(classText)
#print (divs)
#print (text)
#print (soup)
