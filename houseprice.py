from flask import Flask, render_template, jsonify, request
from BeautifulSoup import BeautifulSoup
import urllib3
import time
import threading
import requests
import json


app = Flask(__name__)

loop = True
refinedChelt = []
refinedMent = []
refinedPark = []
refinedBeau = []
priceHistory = []
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

    priceHistory.append(refinedChelt)
    print(str(priceHistory) + "is price history")

    if refinedChelt > priceHistory[0]:
        change = ((int(refinedChelt) - (int(priceHistory[0]))))
    print(str(change) + " is the change")


    getBtc = http.request("GET", "https://bittrex.com/api/v1.1/public/getticker?market=BTC-ETH", preload_content=False)
    soupBtc = BeautifulSoup(getBtc)
    print(soupBtc)
    refinedBtc = soupBtc.result.last
    print(refinedBtc)

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
    return render_template('main.html', REFINEDCHELT=refinedChelt,REFINEDMENT=refinedMent,REFINEDPARK =refinedPark,REFINEDBEAU=refinedBeau)


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
    type(refinedChelt)
    print(str(refinedChelt) + " this is refinedChelt in /_update")
    for each in refinedChelt:
        return jsonify(result1=(str(refinedChelt)))
    for each in refinedMent:
        return jsonify(result2=(str(refinedMent)))
    for each in refinedPark:
        return jsonify(result3=(str(refinedPark)))
    for each in refinedBeau:
        return jsonify(result4=(str(refinedBeau)))


if __name__ == '__main__':
    app.run()

