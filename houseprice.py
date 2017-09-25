from flask import Flask, render_template, jsonify, request
from BeautifulSoup import BeautifulSoup
import urllib3
from datetime import time
import threading
import requests
import json
import re


app = Flask(__name__)

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
    links = []

    realestateurl = "https://www.realestate.com.au/neighbourhoods/"
    postcode = [{"3192": {"price": "100000", "suburb": "cheltenham"}, "3193": {"price": "100000", "suburb":
        "beaumaris"}, "3195": {"price": "500000", "suburb": "parkdale"}, "3194": {"price": "777777",
                                                                                                  "suburb":
                                                                                                      "mentone"}}]

    for item in postcode:
        for each in item:
            priceurl = http.request("GET", realestateurl + item[each]["suburb"] + "-" + (str(each)) + "-vic",preload_content=False)
            soup = BeautifulSoup(priceurl)
            links = soup.findAll("div", {"class": "price strong"})
            postcode[0][each]["price"] = links[2]
            string = postcode[0][each]["price"]
            try:
                blah = (str(string))
                newblah = blah.replace('<div class="price strong">$', "$")
                finalblah = newblah.replace('</div>', "")
                postcode[0][each]["price"] = finalblah
            except:
                postcode[0][each]["price"] = "No DATA!"




def letsThread():
    thread1 = myThread(1, "Thread-1", 1)
    # Start new Threads
    thread1.start()



print("Finished collecting all the content mother fuckers!")

letsThread()

@app.route('/' , methods=['GET','POST'])
def default():
    letsThread()
    links = []

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
    postcode = [{"3192": {"price": "100000", "suburb": "cheltenham"}, "3193": {"price": "100000", "suburb":
        "beaumaris"}, "3195": {"price": "500000", "suburb": "parkdale"}, "3194": {"price": "777777",
                                                                                                  "suburb":
                                                                                                      "mentone"}}]

    for item in postcode:
        for each in item:
            priceurl = http.request("GET", realestateurl + item[each]["suburb"] + "-" + (str(each)) + "-vic",preload_content=False)
            soup = BeautifulSoup(priceurl)
            links = soup.findAll("div", {"class": "price strong"})
            postcode[0][each]["price"] = links[2]
            string = postcode[0][each]["price"]
            try:
                blah = (str(string))
                newblah = blah.replace('<div class="price strong">$', "$")
                finalblah = newblah.replace('</div>', "")
                postcode[0][each]["price"] = finalblah
            except:
                postcode[0][each]["price"] = "No DATA!"


    cryptocompare = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=365&aggregate=3&e=CCCAGG"
    cryptoresponse = http.request("GET", cryptocompare)
    cryptodict = json.loads(cryptoresponse.data.decode('utf-8'))
    daycount = cryptodict
    k = daycount["Data"]
    l = k
    print(l[0]["close"])

    utilities = [{"Electricity": {"Provider": "RED Energy", "ID": "Need Data", "contact": "Need Data",
                                  "payment type": "BPAY"},
                  "Gas": {"Provider": "Origin", "ID": "300008171641", "contact": "13 24 61", "payment type": "BPAY"},
                  "Water": {"Provider": "South East Water", "ID": "Need Data", "contact": "Need Data", \
                                                                                              "payment type": "BPAY"}}]

    insurances = [{"Home": {"Provider": "RACV", "ID": "HOM 612 476 223", "contact":
        "13 RACV",
                                    "payment type": "Direct Debit"}, "Car": {"Provider": "YOUI", "ID": "Need Data", "contact": "13 RACV",
                                    "payment type": "Direct Debit"}, "Life": {"Provider": "OnePath", "ID": "Need Data", "contact": "13 RACV",
                                    "payment type": "Direct Debit"}, "Private Medical": {"Provider": "MediBank",
                                                                                         "ID": "Need Data",
                                                                                         "contact": "Need Data",
                                                                                         "payment type": "Direct Debit"}}]

    loans = [{"Home": {"Provider": "ANZ", "ID": "HNeed Data", "contact": "Need Data",
                                    "payment type": "BPAY"}, "Car": {"Provider": "Alphera", "ID": "Need Data",
                                                                     "contact":
        "Need Data",
                                    "payment type": "Direct Debit"}}]

    cc = [{"Personal": {"Provider": "CommonWealth Bank", "ID": "Need Data", "contact": "Need Data",
                                    "payment type": "Blank"}, "Business": {"Provider": "Bank of Melbourne",
                                                                           "ID": "Need Data", "contact": "Need Data",
                                    "payment type": "Blank"}}]

    bankac = [{"Personal": {"Provider": "CommonWealth Bank", "ID": "Need Data", "contact": "Need Data",
                                    "payment type": "Blank"}, "Business": {"Provider": "Bank of Melbourne",
                                                                           "ID": "Need Data", "contact": "Need Data",
                                    "payment type": "Blank"}}]

    super = [{"Personal": {"Provider": "CommonWealth Bank", "ID": "Need Data", "contact": "Need Data",
                                    "payment type": "Blank"}}]

    gov = [{"Personal": {"Provider": "CommonWealth Bank", "ID": "Need Data", "contact": "Need Data",
                                    "payment type": "Blank"}}]

    savings = [{"Personal": {"Provider": "CommonWealth Bank", "ID": "Need Data", "contact": "Need Data",
                                    "payment type": "Blank"}, "Business": {"Provider": "Bank of Melbourne",
                                                                           "ID": "Need Data", "contact": "Need Data",
                                    "payment type": "Blank"}}]

    metals = [{"Gold": {"AMOUNT": "10oz"}, "Silver": {"AMOUNT": "10oz"}, "Platinum": {"AMOUNT": "10oz"}}]

    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = l

    return render_template('main.html', TICKERS=tickers,CURRENCY=currency,
                           POSTCODE=postcode, DAYCOUNT=daycount, UTILITIES=utilities, INSURANCES=insurances,
                           LOANS=loans, CC=cc, BANKAC=bankac, SUPER=super, SAVINGS=savings, METALS=metals, values=values, labels=labels, legend=legend)




@app.route('/index_one' , methods=['GET', 'POST'])
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


@app.route("/simple_chart")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart.html', values=values, labels=labels, legend=legend)


if __name__ == '__main__':
    app.run()

