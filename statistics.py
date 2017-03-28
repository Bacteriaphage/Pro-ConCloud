from bs4 import BeautifulSoup
import crawler
import re

class CustComm:                             #This class is a structure stores cust, stars and comment for one cust
    cust = ''# {{{
    point = 0.0
    comment = ''
    def __init__(self, cust, point, comment):
        self.cust = cust
        self.point = point
        self.comment = comment
    def __init__(self):
        pass# }}}
crawler.start()
dataArray = []
fopen =  open('reviewPages/review.html', 'r')
soup = BeautifulSoup(fopen, "html.parser")
rawData = soup.find_all(class_="a-section review") #find all comment section in HTML
for row in rawData:
    now = CustComm()
    now.cust = row['id']
    rawPoint = row.find('i').string
    point = re.search('(.+?) out of 5 stars', rawPoint)
    now.point = float(point.group(1))
    rawComment = row.find('span', class_="a-size-base review-text").text #get all comment in one block
    now.comment = rawComment.encode("UTF-8")       #encode with UTF-8 to avoid mistake!!!
    print rawComment
    dataArray.append(now)
for data in dataArray:
    print data.cust, data.point
    print data.comment
fopen.close()
