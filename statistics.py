from bs4 import BeautifulSoup
import crawler
import re

class CustComm:
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
fopen =  open('reviewPages/review.html')
soup = BeautifulSoup(fopen, "html.parser")
rawData = soup.find_all(class_="a-section review")
for row in rawData:
    now = CustComm()
    now.cust = row['id']
    rawPoint = row.find('i').string
    point = re.search('(.+?) out of 5 stars', rawPoint)
    now.point = float(point.group(1))
    rawComment = row.find('span', class_="a-size-base review-text").text
    now.comment = rawComment.encode("UTF-8")
    print rawComment
#    for e in rawComment.find_all('br'):
#        e.decompose()
#    now.comment = rawComment.string
    dataArray.append(now)
for data in dataArray:
    print data.cust, data.point
    print data.comment
fopen.close()
