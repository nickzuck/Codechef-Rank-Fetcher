from bs4 import BeautifulSoup
import urllib2

class Codechef:

    def __init__(self, user_names):
        self.data = []
        self.defaultUrl = "https://codechef.com/users/"
        for name in user_names:
            print "Fetching data for %s ....." %(name)
            self.fetchData(name)
        self.getData()

    def fetchData(self, name):
        self.data.append(urllib2.urlopen(self.defaultUrl + str(name)))
        print "Data retrived for %s" %(name)

    def getData(self):
        print self.data


obj = Codechef(map(str, raw_input().split(" ")))
