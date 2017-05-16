#********************************************
#misc.py
#This part take care of some miscellaneous
#such like help etc.
#********************************************
import statistics
import sys,os
import wordcloud as wc
def helpPrint():
    print "PCcloud.py 1.0 (2017 March 29 9:28PM)"
    print ""
    print "usage: [sudo] python filename [argument]"
    print ""
    print "Arguments:"
    print "    --                No argument(only grap web page and waiting)"
    print "    -p                Give average point for a product"
    print "    -d -p             Draw word cloud for all positive words"
    print "    -d -n             Draw word cloud for all negative words"
    print "    -d -b             Draw word cloud for both pos and neg words"
    print "    -d -a             Draw word cloud for any word appeared in comment"
    print "    --help            Show help page"
def call(dataArray, positive, negative):
    instru = raw_input("input instruction: ")
    while instru != 'exit':
        if instru == 'draw':
            thiswc = wc.WordCloud(background_color = 'white', height = 600, width = 800)
            secondInstru = raw_input("draw what: ")
            while secondInstru != 'exit':
# {{{
                if secondInstru == 'positive':
                    if os.path.exists('posiPic.jpg'):
                        os.remove('posiPic.jpg')
                    adict = statistics.match(positive, dataArray)
                    thiswc.fit_words(adict)
                    thiswc.to_file('posiPic.jpg')
                elif secondInstru == 'negative':
                    if os.path.exists('negaPic.jpg'):
                        os.remove('negaPic.jpg')
                    adict = statistics.match(negative, dataArray)
                    thiswc.fit_words(adict)
                    thiswc.to_file('negaPic.jpg')
                elif secondInstru == 'both':
                    if os.path.exists('PnNPic.jpg'):
                        os.remove('PnNPic.jpg')
                    adict = statistics.match(positive, dataArray)
                    adict.update(statistics.match(negative, dataArray))
                    thiswc.fit_words(adict)
                    thiswc.to_file('PnNPic.jpg')
                elif secondInstru == 'all':
                    if os.path.exists('allPic.jpg'):
                        os.remove('allPic.jpg')
                    adict = statistics.count(dataArray)
                    thiswc.fit_words(adict)
                    thiswc.to_file('allPic.jpg')
                else:
                    print "positive           draw positive words Pic"
                    print "negative           draw negative words Pic"
                    print "both               draw pos and neg words Pic"
                    print "all                draw all words Pic"
                    print "exit               exit draw"
                secondInstru = raw_input("draw what: ")
# }}}
        elif instru == 'avgStar':
            print "The average star of this product is:", statistics.avgPoint(dataArray)
        else:
            print "draw              draw picture"
            print "avgStar           check average star of this product"
        
        instru = raw_input("input instruction: ")
