from bs4 import BeautifulSoup
import crawler
import re

class CustComm:
    cust = ''
    point = 0.0
    comment = ''
    def __init__(self, cust, point, comment):
        self.cust = cust
        self.point = point
        self.comment = comment
    def __init__(self):
        pass
crawler.start()
dataArray = []
soup = BeautifulSoup(open('reviewPages/review.html').read().replace('<br>','') , "html.parser")
rawData = soup.find_all(class_="a-section review")
for row in rawData:
    now = CustComm()
    now.cust = row['id']
    rawPoint = row.find('i').string
    point = re.search('(.+?) out of 5 stars', rawPoint)
    now.point = float(point.group(1))
    now.comment = row.find('span', class_="a-size-base review-text").string
    dataArray.append(now)
for data in dataArray:
    print data.cust, data.point
    print data.comment
