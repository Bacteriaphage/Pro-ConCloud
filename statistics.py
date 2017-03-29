#***************************************
#*statistics.py
#*provide several statistics method
#*be called by PCcloud.py
#***************************************

import concurrent.futures
from string import Template

#single thread
def _positive_match(pSet, dataArray, summary, start, total, gap):
# {{{
    for i in range(start, total, gap):
        localdata = dataArray[i].substitute()
# }}}

#entry for multithread
def positive_match(pSet, dataArray):
# {{{
    size = len(dataArray)
    summary = dict
    with concurrent.futures.ThreadPoolExecutor(max_worker=4) as executor:
        future_to_match = {executor.submit(_positive_match, summary, start, size, 4): start for start in range(1,5)}
        for future in concurrent.futures.as_completed(future_to_match):
            
# }}}

def main():
# {{{
    print "start testing module..."
# }}}

if __name__ == __main__:
    main()
