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
    #prints the url to pass into beautiful soup
    print (url)
    urlOpen = urllib.request.urlopen(url)
    #print the course number
    soup = BeautifulSoup(urlOpen,'html.parser')
    header = soup.find("h2","CDMPageTitle")
    text = header.getText()
    print(text)
    #print(text)
#     divs = soup.find("div","schedule")
#     classInfo = soup.find_all("div","classInfo")
#     #finds all the quarters that the class is offered
#     term = soup.find_all("p","CTIPageSectionHeader")
#     for item in term:
#         pText = item.getText()
#         #for loop on getting all the sections for when a class is offered
#         for info in classInfo:
#             #prints the quarter when class is offerd
#             print(pText)
#             classText = str(info).split("<div>")
#             for element in classText:
#                 #prints the section number
#                 if "Section" in element:
#                     print(element.replace("</div>",""))
#                 #prints the class number for registration
#                 if "Class number" in element:
#                     print(element.replace("</div>",""))
#                 #prints when the classes meet
#                 if "Meeting time" in element:
#                     print(element.replace("</div>",""))
#                 #prints where the classes meet
#                 if "Location" in element:
#                     print(element.replace("</div>",""))
#     #moves to the next required class
#     i = i + 2
# # <<<<<<< Updated upstream
# # =======
# #         if "Instructor" in element:
# #             print(element.replace("<a>",""))
# # >>>>>>> Stashed changes
#     #print(classText)
# #print (divs)
# #print (text)
# #print (soup)
