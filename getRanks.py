from bs4 import BeautifulSoup
import urllib2

class Codechef:

    def __init__(self, user_names):
        from time import sleep
        self.data = []
        self.defaultUrl = "https://codechef.com/users/"
        for name in user_names:
            print "Fetching data for %s ....." %(name)
            try:
                self.fetchData(name)
                #print "Sleeping for 1 sec"
                #sleep(1)
            except urllib2.HTTPError:
                print "Server Error for %s" %(name)
                print "Will retry after 3 secs"
                sleep(3)
                print "Retrying ...." 
                self.fetchData(name)

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
        #print "HX DATA  = ", hxData
        #print  "Type of hx data " , type(hxData)
        ranks = []
        for i in hxData:
            temp = str(i.string)
            if temp == 'NA' or temp == 'None' or temp == '' or temp == None:
                temp = 'NA'
            ranks.append(temp)
        #print "Ranks", ranks
        return ranks

    def printRanks(self, name, ranks):
        
        print " ---------------RANKS FOR %s  are :------------" %(name) 

        # Fix for the person who haven't attended a single contest yet
        if len(ranks) == 3:
            self.printEmptyRanks()
        else:
            print "Long Contest -- %s | %s" %(ranks[0] , ranks[1])
            print "Cook Off     -- %s | %s" %(ranks[2], ranks[3])
            print "Lunch Time   -- %s | %s " %(ranks[4] , ranks[5])


    def printEmptyRanks(self):
        print "Long Contest -- NA" 
        print "Cook Off     -- NA" 
        print "Lunch Time   -- NA"

    def getData(self):
        print self.data


obj = Codechef(map(str, raw_input().split(" ")))
obj.getRanks()
