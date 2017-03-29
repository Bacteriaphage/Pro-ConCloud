from bs4 import BeautifulSoup
import crawler,statistics
import re
import concurrent.futures
import wordcloud as wc
import sys,os,glob
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
#extract raw data in to CustComm data structure
def extract_info(start, total, gap):
# {{{
    dataArray=[]
    for i in range(start, total+1, gap):
        fopen = open('reviewPages/review'+str(i)+'.html', 'r')
        soup = BeautifulSoup(fopen, "html.parser")
        rawData = soup.find_all(class_="a-section review") #find all comment section in HTML
        fopen.close()
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
    return dataArray
# }}}
#read pos and neg word from files
def fillDict(pos, neg):
# {{{
    nfopen = open('negative.txt', 'r')
    pfopen = open('positive.txt', 'r')
    for line in pfopen:
        pos.add(line.strip())
    for line in nfopen:
        neg.add(line.strip())
    pfopen.close()
    nfopen.close()
# }}}

def main(argv):
# {{{
    filenum = crawler.start()
    print "crawling web page..."
    print "generate", str(filenum), "files"
    dataArray = []
    positive = set()
    negative = set()

    print "extracting data..."
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_ext = {executor.submit(extract_info, start, filenum, 4): start for start in range(1,5)}
        for future in concurrent.futures.as_completed(future_to_ext):
            dataArray.extend(future.result())
    print "extract",len(dataArray),"comments"
    fillDict(positive, negative)
    print "read all sample word"
    if argv[1] == '-d':
        if len(argv) == 2:
            print "invalid option"
        elif argv[2] == '-p':
            adict = statistics.match(positive, dataArray)
        elif argv[2] == '-n':
            adict = statistics.match(negative, dataArray)
        thiswc = wc.WordCloud(background_color='white', height=600, width=800)
        thiswc.fit_words(adict)
        if argv[2] == '-p':
            if os.path.exists('posiPic.jpg'):
                os.remove('posiPic.jpg')
            thiswc.to_file("posiPic.jpg")
        elif argv[2] == '-n':
            if os.path.exists('negaPic.jpg'):
                os.remove('negaPic.jpg')
            thiswc.to_file("negaPic.jpg")
# }}}
if __name__ == '__main__':
    main(sys.argv)
