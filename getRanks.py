from bs4 import BeautifulSoup
import urllib2

class Codechef:

    def __init__(self, user_names):
        from time import sleep
        self.data = []
        self.defaultUrl = "https://codechef.com/users/"
        for name in user_names:
            print "Fetching data for %s ....." %(name)
            self.fetchData(name)
            print "Sleeping for 1 sec"
            sleep(1)

    def fetchData(self, name):
        self.data.append({name : urllib2.urlopen(self.defaultUrl + str(name))})
        print "Data retrived for %s" %(name)

        
    def getRanks(self):
        data = self.data
        for index, value in enumerate(data):
            html = (value.values()[0]).read()
            ranks = self.collectRanks(html)
            self.printRanks(value.keys()[0], ranks)


    def collectRanks(self, html):
        # Beautiful Soup in Action ... Scraping begins now
        bsData = BeautifulSoup(html, "html.parser")
        # Since on codechef the ranks are surrounded by the special tag hx
        hxData = bsData.findAll("hx") 
        ranks = []
        for i in hxData:
            temp = str(i.string)
            if temp == 'NA' or temp == 'None':
                temp = 'NA'
            ranks.append(temp)
        return ranks

    def printRanks(self, name, ranks):
        print " ---------------RANKS FOR %s  are :------------" %(name) 
        print "Long Contest -- %s | %s" %(ranks[0] , ranks[1])
        print "Cook Off     -- %s | %s" %(ranks[2], ranks[3])
        print "Lunch Time   -- %s | %s " %(ranks[4] , ranks[5])
            
    def getData(self):
        print self.data


obj = Codechef(map(str, raw_input().split(" ")))
obj.getRanks()
