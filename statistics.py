from bs4 import BeautifulSoup
import crawler
import re
import concurrent.futures

class CustComm:                             #This class is a structure stores cust, stars and comment for one cust
# {{{
    _cust = ''
    _point = 0.0
    _comment = ''
    def __init__(self, cust, point, comment):
        self._cust = cust
        self._point = point
        self._comment = comment
    def __init__(self):
        pass
# }}}

def extract_info(dataArray, start, total, gap):
# {{{
    for i in range(start, total+1, gap):
        fopen =  open('reviewPages/review'+str(i)+'.html', 'r')
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
            dataArray.append(now)
#        for data in dataArray:
#            print data.cust, data.point
#            print data.comment
        fopen.close()
    return 'finish at '+str(i)+'page'
# }}}
def main():
# {{{
    filenum = crawler.start()
    print "crawling web page..."
    print "generate", str(filenum), "files"
    dataArray = []
    print "extracting data..."
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_ext = {executor.submit(extract_info, dataArray, start, filenum, 4): start for start in range(1,5)}
        for future in concurrent.futures.as_completed(future_to_ext):
            print future.result()
    print "extract",len(dataArray),"comment"
# }}}
if __name__ == '__main__':
    main()

