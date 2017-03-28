import urllib2,os,sys,time

def start():
        browser = urllib2.build_opener()

        browser.addheaders=[('User-agent', 'Mozilla/5.0')]

        if not os.path.exists('reviewPages'):os.mkdir('reviewPages')

        url = raw_input("input URL here: ")
        print 'start crawler...'
        try:
            response = browser.open(url)
        except Exception as e:
            error_type, error_obj, error_info = sys.exc_info()
            print 'ERROR FOR LINK',url
            print error_type, 'Line:', error_info.tb_lineno

        myHTML=response.read()

        fwriter=open('reviewPages/'+'review.html','w')
        fwriter.write(myHTML)
        fwriter.close()

def main():
    print 'module test...'
    start()
if __name__ == "__main__":
    main()
