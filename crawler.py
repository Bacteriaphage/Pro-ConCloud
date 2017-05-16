#**********************************************
#*crawler.py
#*crawling up to 10 pages comment to local disk
#*waiting for next progress
#**********************************************
import urllib2,os,sys,time,glob,cookielib

def start():
        jar = cookielib.LWPCookieJar("cookies")
        browser = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
        
        browser.addheaders=[('User-agent', 'Mozilla/5.0')]

        if not os.path.exists('reviewPages'):os.mkdir('reviewPages')
        else:
            for delfile in glob.glob('reviewPages/*.*'): #delete all prev files
                os.remove(delfile)


        url = raw_input("input URL here: ")
        print 'start crawler...'
        i = 1
        bad = False
        for i in range(1,20):
                try:
                    response = browser.open(url+'&pageNumber='+str(i))
                except Exception as e:
                    error_type, error_obj, error_info = sys.exc_info()
                    print 'ERROR FOR LINK',url
                    print error_type, 'Line:', error_info.tb_lineno
                    bad = True
                    break

                myHTML=response.read()

                fwriter=open('reviewPages/review'+str(i)+'.html','w')
                fwriter.write(myHTML)
                fwriter.close()
                time.sleep(.01)
        if bad:
            return i-1
        else:
            return i

def main():
    print 'module test...'
    start()
if __name__ == "__main__":
    main()
