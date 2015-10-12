from bs4 import BeautifulSoup
import urllib.request

list = ['animation-animator.txt','animation-ta.txt','BIT.txt','cinema-post.txt','cinema-production.txt',
    'cinema-sound.txt','cns-governance.txt','cns-networkSecurity.txt','cns-security.txt','comp-finance.txt',
    'comp-science.txt','e-commerce.txt','game-development.txt','hci.txt','health-informatics.txt',
    'is-bi.txt','is-bs.txt','is-da.txt','is-enterprise.txt','is-standard.txt','it-project.txt',
    'media-arts.txt','network-engineering.txt','pa-comp.txt','pa-healthcare.txt','pa-hospitality.txt',
    'pa-marketing.txt','se-entrepreneurship.txt','se-game.txt','se-project.txt','se-software.txt','se-softwareDev.txt']
for item in list:
    file = open(item, "r") #file of  class required for degree. Can change to whatever we need
    line = file.readline()
    str = line.replace('|',' ')
    list1 = str.split(' ')
    i = 0
    while i < len(list1):
        subject = list1[i]
        cNum = list1[i + 1]
        url = item + "http://www.cdm.depaul.edu/academics/pages/courseinfo.aspx?Subject=" + subject + "&CatalogNbr=" + cNum
        print (url)
        # need to save in a list
        i = i + 2
