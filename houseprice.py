from flask import Flask, render_template, jsonify, request
from BeautifulSoup import BeautifulSoup
import urllib3
import time
import threading
import requests
import json


app = Flask(__name__)

loop = True
refinedChelt = "$"
refinedMent = "$"
refinedPark = "$"
refinedBeau = "$"
priceHistory = []
soupUsd = []
soupEth = []
soupSc = []
soupStrat = []
soupLsk = []
soupLbc = []
change = 0
http = urllib3.PoolManager()


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        getContent()
        print "Exiting " + self.name

def getContent():
    global change
    global loop
    global refinedChelt
    global refinedMent
    global refinedPark
    global refinedBeau
    global soupUsd
    global soupEth
    global soupSc
    global soupStrat
    global soupLsk
    global soupLbc


    urlChelt = http.request("GET", "https://www.realestate.com.au/neighbourhoods/cheltenham-3192-vic", preload_content=False)
    urlMent = http.request("GET", "https://www.realestate.com.au/neighbourhoods/mentone-3194-vic", preload_content=False)
    urlPark = http.request("GET", "https://www.realestate.com.au/neighbourhoods/parkdale-3195-vic", preload_content=False)
    urlBeau = http.request("GET", "https://www.realestate.com.au/neighbourhoods/beaumaris-3193-vic", preload_content=False)

    soupChelt = BeautifulSoup(urlChelt)
    soupMent = BeautifulSoup(urlMent)
    soupPark = BeautifulSoup(urlPark)
    soupBeau = BeautifulSoup(urlBeau)

    linksChelt = soupChelt.findAll("div", {"class": "price strong"})
    linksMent = soupMent.findAll("div", {"class": "price strong"})
    linksPark = soupPark.findAll("div", {"class": "price strong"})
    linksBeau = soupBeau.findAll("div", {"class": "price strong"})

    refinedChelt = linksChelt[2]
    refinedMent = linksMent[2]
    refinedPark = linksPark[2]
    refinedBeau = linksBeau[2]

    print(str(refinedChelt) + "is refinedChelt")
    print(str(refinedMent) + "is refinedMent")
    print(str(refinedPark) + "is refinedPark")
    print(str(refinedBeau) + "is refinedBeau")

    # priceHistory.append(refinedChelt)
    # print(str(priceHistory) + "is price history")
    #
    # if refinedChelt > priceHistory[0]:
    #     change = ((int(refinedChelt) - (int(priceHistory[0]))))
    # print(str(change) + " is the change")


    # getusd = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=USDT-BTC", preload_content=False)
    # soupUsd = [BeautifulSoup(getusd)]
    # response = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=USDT-BTC")
    # usddict = json.loads(response.data.decode('utf-8'))
    # usdmain = usddict['result']
    # usdlast = usdmain['Last']

    geteth = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-ETH", preload_content=False)
    soupEth = [BeautifulSoup(geteth)]

    getsc = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-SC", preload_content=False)
    soupSc = [BeautifulSoup(getsc)]

    getstrat = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-STRAT",
                            preload_content=False)
    soupStrat = [BeautifulSoup(getstrat)]

    getlsk = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-LSK", preload_content=False)
    soupLsk = [BeautifulSoup(getlsk)]

    getlbc = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-LBC",
                            preload_content=False)
    soupLbc = [BeautifulSoup(getlbc)]



def letsThread():
    thread1 = myThread(1, "Thread-1", 1)
    # Start new Threads
    thread1.start()



print("Finished collecting all the content mother fuckers!")

letsThread()

@app.route('/' , methods=['GET','POST'])
def default():
    letsThread()
    global refinedChelt
    global refinedMent
    global refinedPark
    global refinedBeau
    global soupUsd
    global soupEth
    global soupSc
    global soupStrat
    global soupLsk
    global soupLbc

    responsebtc = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=USDT-BTC")
    usddictbtc = json.loads(responsebtc.data.decode('utf-8'))
    usdmainbtc = usddictbtc['result']
    usdlastbtc = usdmainbtc['Last']
    usdfloatbtc = (str(usdlastbtc))

    responseeth = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-ETH")
    usddicteth = json.loads(responseeth.data.decode('utf-8'))
    usdmaineth = usddicteth['result']
    usdlasteth = usdmaineth['Last']
    usdfloateth = (str(usdlasteth))

    responsesc = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-SC")
    usddictsc = json.loads(responsesc.data.decode('utf-8'))
    usdmainsc = usddictsc['result']
    usdlastsc = usdmainsc['Last']
    usdfloatsc = (str(usdlastsc))

    responsestrat = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-STRAT")
    usddictstrat = json.loads(responsestrat.data.decode('utf-8'))
    usdmainstrat = usddictstrat['result']
    usdlaststrat = usdmainstrat['Last']
    usdfloatstrat = (str(usdlaststrat))

    responselsk = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-LSK")
    usddictlsk = json.loads(responselsk.data.decode('utf-8'))
    usdmainlsk = usddictlsk['result']
    usdlastlsk = usdmainlsk['Last']
    usdfloatlsk = (str(usdlastlsk))

    responselbc = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-LBC")
    usddictlbc = json.loads(responselbc.data.decode('utf-8'))
    usdmainlbc = usddictlbc['result']
    usdlastlbc = usdmainlbc['Last']
    usdfloatlbc = (str(usdlastlbc))

    responsefixeraus = http.request("GET", "http://api.fixer.io/latest?symbols=USD,GBP")
    usddictfixeraus = json.loads(responsefixeraus.data.decode('utf-8'))
    # usdmainfixeraus = usddictfixeraus['rates']
    # usdlastfixeraus = usdmainfixeraus['USD']
    # usdfloatfixeraus = (str(usdlastfixeraus))

    return render_template('main.html',SOUPBTC=usdfloatbtc,SOUPLSK=usdfloatlsk,SOUPLBC=usdfloatlbc,
                           SOUPSTRAT=usdfloatstrat,
                           SOUPSC=usdfloatsc,\
                                                                                                  SOUPETH=usdfloateth,
                           REFINEDCHELT=refinedChelt,
                           REFINEDMENT=refinedMent,REFINEDPARK \
        =refinedPark,REFINEDBEAU=refinedBeau,)


@app.route('/index_one' , methods=['GET','POST'])
def login_one():
    return render_template('index_one.html')


@app.route('/index_two' , methods=['GET','POST'])
def login_two():
    return render_template('index_two.html')


@app.route('/index_three' , methods=['GET','POST'])
def login_three():
    return render_template('index_three.html')


@app.route('/knight' , methods=['GET','POST'])
def knight():
    return render_template('index_knight.html')


@app.route('/niceadmin' , methods=['GET','POST'])
def niceadmin():
    return render_template('NiceAdminhtml/index_niceadmin.html')


@app.route('/nicedocumentation' , methods=['GET','POST'])
def nicedoc():
    return render_template('NiceAdminhtml/documentation.html')


@app.route('/nicelogin' , methods=['GET','POST'])
def nicelogin():
    return render_template('NiceAdminhtml/login.html')


@app.route('/niceform_component' , methods=['GET','POST'])
def nicecomp():
    return render_template('NiceAdminhtml/form_component.html')


@app.route('/niceform_validation' , methods=['GET','POST'])
def nicevalid():
    return render_template('NiceAdminhtml/form_validation.html')



@app.route('/free' , methods=['GET','POST'])
def free():
    return render_template('Free/index.html')


@app.route('/_update')
def add_pricing():
    letsThread()
    global refinedChelt
    global refinedMent
    global refinedPark
    global refinedBeau
    global soupUsd
    global soupEth
    global soupSc
    global soupStrat
    global soupLsk
    global soupLbc

    responsebtc = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=USDT-BTC")
    usddictbtc = json.loads(responsebtc.data.decode('utf-8'))
    usdmainbtc = usddictbtc['result']
    usdlastbtc = usdmainbtc['Last']
    usdfloatbtc = (str(usdlastbtc))

    responseeth = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-ETH")
    usddicteth = json.loads(responseeth.data.decode('utf-8'))
    usdmaineth = usddicteth['result']
    usdlasteth = usdmaineth['Last']
    usdfloateth = (str(usdlasteth))

    responsesc = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-SC")
    usddictsc = json.loads(responsesc.data.decode('utf-8'))
    usdmainsc = usddictsc['result']
    usdlastsc = usdmainsc['Last']
    usdfloatsc = (str(usdlastsc))

    responsestrat = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-STRAT")
    usddictstrat = json.loads(responsestrat.data.decode('utf-8'))
    usdmainstrat = usddictstrat['result']
    usdlaststrat = usdmainstrat['Last']
    usdfloatstrat = (str(usdlaststrat))

    responselsk = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-LSK")
    usddictlsk = json.loads(responselsk.data.decode('utf-8'))
    usdmainlsk = usddictlsk['result']
    usdlastlsk = usdmainlsk['Last']
    usdfloatlsk = (str(usdlastlsk))

    responselbc = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-LBC")
    usddictlbc = json.loads(responselbc.data.decode('utf-8'))
    usdmainlbc = usddictlbc['result']
    usdlastlbc = usdmainlbc['Last']
    usdfloatlbc = (str(usdlastlbc))

    type(refinedChelt)
    type(refinedMent)
    print(str(refinedChelt) + " this is refinedChelt in /_update")
    print(str(refinedMent) + " this is refinedMent in /_update")

    # for each in refinedChelt:
    return float(result5=(str(usdlastbtc))),float(result6=(str(usdlasteth))),float(result7=(str(usdlastsc))),\
               float(result8=(str(usdlaststrat))),float(result9=(str(usdlastlsk))),float(result10=(str(usdlastlbc))),\
               jsonify(result1=(str(refinedChelt)),result2=(str(refinedMent)),
                                                                                   result3=(str(refinedPark)),
                       result4=(str(refinedBeau)))


if __name__ == '__main__':
    app.run()

