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
        self.data.append({name : urllib2.urlopen(self.defaultUrl + str(name))})
        print "Data retrived for %s" %(name)

        
    def getRanks(self):
        data = self.data
        for index, value in enumerate(data):
            html =  0


    def collectRanks(self):
        pass

    def printRanks(self):
        pass

    def getData(self):
        print self.data


obj = Codechef(map(str, raw_input().split(" ")))
obj.getRanks()
