#***************************************
#*statistics.py
#*provide several statistics method
#*be called by PCcloud.py
#***************************************

import concurrent.futures
from string import Template
import re
import os, sys

#single thread
def _match(aSet, dataArray, start, total, gap):
# {{{
    summary = dict()
    try:
        for i in range(start, total, gap):
            regex = re.compile('[^a-zA-z \n]')
            wordList = regex.sub('',dataArray[i].comment).split()
            for word in wordList:
                lowWord = word.lower()
                if lowWord in aSet:
                    if lowWord in summary:
                        summary[lowWord]+= 1
                    else:
                        summary[lowWord] = 1
    except Exception as exc:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print "inner exception: ", exc_tb.tb_lineno
    return summary
# }}}

#entry for multithread
def match(aSet, dataArray):  #any set n or p
# {{{
    size = len(dataArray)
    summary = dict()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_match = {executor.submit(_match, aSet, dataArray, start, size, 4): start for start in range(1,5)}
        for future in concurrent.futures.as_completed(future_to_match):
            try:
                data = future.result()
                for key in data.keys():
                    if key in summary:
                        summary[key]+=data[key]
                    else:
                        summary[key]=data[key]
            except Exception as exc:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print("generate exception %s"% exc, exc_tb.tb_lineno)
    return summary
#    for key in summary.keys():
#        print key, summary[key]
# }}}

def main():
# {{{
    print "start testing module..."
    
# }}}

if __name__ == '__main__':
    main()
