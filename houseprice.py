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
    tickers = [
                {"USDT-BTC":
                     {"pair": "USD",
                      "colour": "rgba(0, 192, 192, 1)",
                      "Last": 0,
                      "url": "BTC",
                      "labels": [],
                      "values": [],
                      "30ma": 0,
                      "60ma": 0,
                      "90ma": 0,
                      "quantity": 500
                      },
                 "BTC-ETH":
                     {"pair": "BTC",
                      "colour": "rgba(75, 0, 192, 1)",
                      "Last": 0,
                      "url": "ETH",
                      "labels": [],
                      "values": [],
                      "30ma": 0,
                      "60ma": 0,
                      "90ma": 0,
                      "quantity": 100.94
                      },
                 "BTC-SC":
                     {"pair": "BTC",
                      "colour": "rgba(75, 192, 0, 1)",
                      "Last": 0,
                      "url": "SC",
                      "labels": [],
                      "values": [],
                      "30ma": 0,
                      "60ma": 0,
                      "90ma": 0,
                      "quantity": 89073
                      },
                 "BTC-STRAT":
                     {"pair": "BTC",
                      "colour": "rgba(100, 192, 192, 255)",
                      "Last": 0,
                      "url": "STRAT",
                      "labels": [],
                      "values": [],
                      "30ma": 0,
                      "60ma": 0,
                      "90ma": 0,
                      "quantity": 586
                      },
                 "BTC-LSK":
                     {"pair": "BTC",
                      "colour": "rgba(75, 255, 255, 1)",
                      "Last": 0,
                      "url": "LSK",
                      "labels": [],
                      "values": [],
                      "30ma": 0,
                      "60ma": 0,
                      "90ma": 0,
                      "quantity": 466
                      },
                 "BTC-LBC":
                     {"pair": "BTC",
                      "colour": "rgba(75, 192, 192, 1)",
                      "Last": 0,
                      "url": "LBC",
                      "labels": [],
                      "values": [],
                      "30ma": 0,
                      "60ma": 0,
                      "90ma": 0,
                      "quantity": 333
                      }
                 }]

    print("loaded tickers dictionary")

    for each in tickers[0]:

        response = http.request("GET", bittick + each)
        usddict = json.loads(response.data.decode('utf-8'))
        usdmain = usddict['result']
        usdlast = usdmain['Last']
        tickers[0][each]["Last"] = (str(usdlast))

    fixer = "http://api.fixer.io/latest?base=AUD"
    currency = {'USD': 0, 'GBP': 0, 'EUR': 0}

    for each in currency:

        responsefixer = http.request("GET", fixer)
        usddictfixer = json.loads(responsefixer.data.decode('utf-8'))
        usdmainfixer = usddictfixer['rates']
        usdratefixer = usdmainfixer[each]
        currency[each] = (str(usdratefixer))

    realestateurl = "https://www.realestate.com.au/neighbourhoods/"
    postcode = [{"3192": {"price": "100000", "suburb": "cheltenham"}, "3193": {"price": "100000", "suburb":
        "beaumaris"}, "3195": {"price": "500000", "suburb": "parkdale"}, "3194": {"price": "777777",
                                                                                                  "suburb": "mentone"}}]
    print("just loaded postcode successfully")

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

    print("looping through postcodes")

    legend = 'Price'

    for key in tickers[0]:
        print("building URL to retrieve " + key)
        # url = tickers[0][key]["url"]
        # pair = tickers[0][key]["pair"]
        print(tickers[0][key]["url"])
        print(tickers[0][key]["pair"])
        cryptocompare = "https://min-api.cryptocompare.com/data/histoday?fsym=" + tickers[0][key]["url"] + \
                        "&tsym=" + tickers[0][key]["pair"] + "&limit=365&aggregate=3&e=CCCAGG"
        print(cryptocompare)
        cryptoresponse = http.request("GET", cryptocompare)
        cryptodict = json.loads(cryptoresponse.data.decode('utf-8'))
        daycount = cryptodict
        k = daycount["Data"]
        # print(str(k) + "is K")


        # if thirtyMa == (tickers[0][key]["close"]):
        #     thirtyMaBreak = False
        # else:
        #     thirtyMaBreak = True
        #
        # if sixtyMa > (tickers[0][key]["close"]):
        #     sixtyMaBreak = False
        # else:
        #     sixtyMaBreak = True
        #
        # if ninetyMa > (tickers[0][key]["close"]):
        #     ninetyMaBreak = False
        # else:
        #     ninetyMaBreak = True



        for each in k:
            close = each["close"]
            tickers[0][key]["values"].append(close)
            time = each["time"]
            tickers[0][key]["labels"].append(time)

        thirtyMa = sum(tickers[0][key]["values"][-30:])/30
        tickers[0][key]["30ma"] = thirtyMa
        sixtyMa = sum(tickers[0][key]["values"][-60:])/60
        tickers[0][key]["60ma"] = sixtyMa
        ninetyMa = sum(tickers[0][key]["values"][-90:])/90
        tickers[0][key]["90ma"] = ninetyMa
        print((str(tickers[0][key]["30ma"])) + " is the thirtyMa")
        print((str(tickers[0][key]["60ma"])) + " is the sixtyMa")
        print((str(tickers[0][key]["90ma"])) + " is the ninetyMa")

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

    return render_template('main.html', TICKERS=tickers, CURRENCY=currency,
                           POSTCODE=postcode, DAYCOUNT=daycount, UTILITIES=utilities, INSURANCES=insurances,
                           LOANS=loans, CC=cc, BANKAC=bankac, SUPER=super, SAVINGS=savings, METALS=metals,
                           LEGEND=legend, THIRTYMA=thirtyMa, SIXTYMA=sixtyMa, NINETYMA=ninetyMa)




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

