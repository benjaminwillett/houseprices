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


    realestateurl = "https://www.realestate.com.au/neighbourhoods/"
    postcode = [{3192:{"price":0,"suburb":"cheltenham"},3195:{"price":0,"suburb":"mentone"},3193:{"price":0,
                                                                                                  "suburb":"parkdale"}}]

    for item in postcode:
        for each in item:

            priceurl = http.request("GET", realestateurl + item[each]["suburb"] + "-" + (str(each)) + "-vic",
                                    preload_content=False)
            soup = BeautifulSoup(priceurl)
            links = soup.findAll("div", {"class": "price strong"})
            print((type(links)) + "is the type of object now winnnnnnn")
            print()
            print(len(links))
            refined = links[0]
            postcode[0][each]["price"] = (str(refined))


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

    bittick = "https://bittrex.com/api/v1.1/public/getticker?market="
    tickers = {"USDT-BTC":0,"BTC-ETH":0,"BTC-SC":0,"BTC-STRAT":0,"BTC-LSK":0,"BTC-LBC":0}

    for each in tickers:

        response = http.request("GET", bittick + each)
        usddict = json.loads(response.data.decode('utf-8'))
        usdmain = usddict['result']
        usdlast = usdmain['Last']
        tickers[each] = (str(usdlast))

    fixer = "http://api.fixer.io/latest?base=AUD"
    currency = {'USD':0,'GBP':0,'EUR':0}

    for each in currency:

        responsefixer = http.request("GET", fixer)
        usddictfixer = json.loads(responsefixer.data.decode('utf-8'))
        usdmainfixer = usddictfixer['rates']
        usdratefixer = usdmainfixer[each]
        currency[each] = (str(usdratefixer))

    realestateurl = "https://www.realestate.com.au/neighbourhoods/"
    postcode = [{3192:{"price":0,"suburb":"cheltenham"},3195:{"price":0,"suburb":"mentone"},3193:{"price":0,"suburb":"parkdale"}}]

    for item in postcode:
        for each in item:

            priceurl = http.request("GET", realestateurl + item[each]["suburb"] + "-" + (str(each))  + "-vic",
                                    preload_content=False)
            soup = BeautifulSoup(priceurl)
            links = soup.findAll("div", {"class": "price strong"})
            refined = links[0]
            postcode[0][each]["price"] = (str(refined))


    return render_template('main.html',TICKERS=tickers,CURRENCY=currency,
                           POSTCODE=postcode)


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



if __name__ == '__main__':
    app.run()

