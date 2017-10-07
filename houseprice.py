from flask import Flask, render_template, jsonify, request
from BeautifulSoup import BeautifulSoup
import urllib3
import threading
import json
import os


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
        getcontent()
        print "Exiting " + self.name


def getcontent():

    realestateurl = "https://www.realestate.com.au/neighbourhoods/"
    postcode = [{"3192": {"price": "100000", "suburb": "cheltenham"},
                 "3193": {"price": "100000", "suburb": "beaumaris"},
                 "3195": {"price": "500000", "suburb": "parkdale"},
                 "3194": {"price": "777777", "suburb": "mentone"}}]

    for item in postcode:
        for each in item:
            priceurl = http.request("GET", realestateurl +
                                    item[each]["suburb"] + "-" + (str(each)) + "-vic", preload_content=False)
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


def letsthread():
    thread1 = myThread(1, "Thread-1", 1)
    # Start new Threads
    thread1.start()

print("Finished collecting all the content mother fuckers!")

letsthread()


@app.route('/', methods=['GET', 'POST'])
def default():
    letsthread()

    bittick = "https://bittrex.com/api/v1.1/public/getticker?market="
    tickers = [
                {"USDT-BTC":
                     {"pair": "USD",
                      "colour": "rgba(255, 153, 151, 1)",
                      "Last": 0,
                      "url": "BTC",
                      "labels": [],
                      "values": [],
                      "30ma": 0,
                      "60ma": 0,
                      "90ma": 0,
                      "quantity": 0,
                      "value": 0,
                      },
                 "BTC-ETH":
                     {"pair": "BTC",
                      "colour": "rgba(51, 51, 255, 1)",
                      "Last": 0,
                      "url": "ETH",
                      "labels": [],
                      "values": [],
                      "30ma": 0,
                      "60ma": 0,
                      "90ma": 0,
                      "quantity": 0.94,
                      "value": 0,
                      },
                 "BTC-SC":
                     {"pair": "BTC",
                      "colour": "rgba(51, 255, 51, 1)",
                      "Last": 0,
                      "url": "SC",
                      "labels": [],
                      "values": [],
                      "30ma": 0,
                      "60ma": 0,
                      "90ma": 0,
                      "quantity": 89073,
                      "value": 0,
                      },
                 "BTC-STRAT":
                     {"pair": "BTC",
                      "colour": "rgba(255, 0, 127, 1)",
                      "Last": 0,
                      "url": "STRAT",
                      "labels": [],
                      "values": [],
                      "30ma": 0,
                      "60ma": 0,
                      "90ma": 0,
                      "quantity": 586,
                      "value": 0,
                      },
                 "BTC-LSK":
                     {"pair": "BTC",
                      "colour": "rgba(51, 153, 255, 1)",
                      "Last": 0,
                      "url": "LSK",
                      "labels": [],
                      "values": [],
                      "30ma": 0,
                      "60ma": 0,
                      "90ma": 0,
                      "quantity": 466,
                      "value": 0,
                      },
                 "BTC-LBC":
                     {"pair": "BTC",
                      "colour": "rgba(255, 255, 51, 1)",
                      "Last": 0,
                      "url": "LBC",
                      "labels": [],
                      "values": [],
                      "30ma": 0,
                      "60ma": 0,
                      "90ma": 0,
                      "quantity": 333,
                      "value": 0,
                      }
                 }]

    print("loaded tickers dictionary")

    for each in tickers[0]:

        response = http.request("GET", bittick + each)
        usddict = json.loads(response.data.decode('utf-8'))
        usdmain = usddict['result']
        usdlastclean = usdmain
        usdlast = (float(usdlastclean['Last']))
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
    postcode = [{"3192": {"price": "100000", "suburb": "cheltenham"},
                 "3193": {"price": "100000", "suburb": "beaumaris"},
                 "3195": {"price": "500000", "suburb": "parkdale"},
                 "3194": {"price": "777777", "suburb": "mentone"}}]

    print("just loaded postcode successfully")

    for item in postcode:
        for each in item:
            priceurl = http.request("GET", realestateurl + item[each]["suburb"]
                                    + "-" + (str(each)) + "-vic", preload_content=False)
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
        print(tickers[0][key]["url"])
        print(tickers[0][key]["pair"])
        cryptocompare = "https://min-api.cryptocompare.com/data/histoday?fsym=" + tickers[0][key]["url"] + \
                        "&tsym=" + tickers[0][key]["pair"] + "&limit=365&aggregate=3&e=CCCAGG"
        print(cryptocompare)
        cryptoresponse = http.request("GET", cryptocompare)
        cryptodict = json.loads(cryptoresponse.data.decode('utf-8'))
        daycount = cryptodict
        k = daycount["Data"]

        for each in k:
            close = each["close"]
            tickers[0][key]["values"].append(float(close))
            time = each["time"]
            tickers[0][key]["labels"].append(time)

        thirtyMa = (float(sum(tickers[0][key]["values"][-30:])/30))
        tickers[0][key]["30ma"] = thirtyMa
        sixtyMa = (float(sum(tickers[0][key]["values"][-60:])/60))
        tickers[0][key]["60ma"] = sixtyMa
        ninetyMa = (float(sum(tickers[0][key]["values"][-90:])/90))
        tickers[0][key]["90ma"] = ninetyMa
        print((str(tickers[0][key]["30ma"])) + " is the thirtyMa")
        print((str(tickers[0][key]["60ma"])) + " is the sixtyMa")
        print((str(tickers[0][key]["90ma"])) + " is the ninetyMa")

    for each in tickers[0]:
        lastHol = tickers[0][each]["Last"]
        quantity = tickers[0][each]["quantity"]
        print(str(type(lastHol)) + " is " + each + " " + lastHol)
        print(str(type(quantity)) + " is quantity " + (str(quantity)))
        lastholcon = float(lastHol)
        print(str(type(lastholcon)) + " is lastHolcon")
        # print(str(type(quantityCon)) + " is quantityCon")
        holdingsval = (str(lastholcon * quantity))
        tickers[0][each]["value"] = holdingsval
        print("BTC " + str(tickers[0][each]["value"]) + " is the value of the portfolio")

    totalval = 0.0
    for each in tickers[0]:
        val = float(tickers[0][each]["value"])
        totalval = (float(totalval) + val)
        print(str(totalval) + " is the totalval")

    utilities = [{"Electricity":
                    {"Provider": "RED Energy",
                     "ID": "Need Data",
                     "contact": "Need Data",
                     "payment type": "BPAY"},
                  "Gas":
                    {"Provider": "Origin",
                     "ID": "300008171641",
                     "contact": "13 24 61",
                     "payment type": "BPAY"},
                  "Water":
                    {"Provider": "South East Water",
                     "ID": "Need Data",
                     "contact": "Need Data",
                     "payment type": "BPAY"}}]

    insurances = [{"Home":
                    {"Provider": "RACV",
                     "ID": "HOM 612 476 223",
                     "contact": "13 RACV",
                     "payment type": "Direct Debit"},
                   "Car":
                    {"Provider": "YOUI",
                     "ID": "Need Data",
                     "contact": "13 RACV",
                     "payment type": "Direct Debit"},
                   "Life":
                    {"Provider": "OnePath",
                     "ID": "Need Data",
                     "contact": "13 RACV",
                     "payment type": "Direct Debit"},
                   "Private Medical":
                    {"Provider": "MediBank",
                     "ID": "Need Data",
                     "contact": "Need Data",
                     "payment type": "Direct Debit"}}]

    loans = [{"Home":
                  {"Provider": "ANZ",
                   "ID": "HNeed Data",
                   "contact": "Need Data",
                   "payment type": "BPAY"},
              "Car":
                  {"Provider": "Alphera",
                   "ID": "Need Data",
                   "contact": "Need Data",
                   "payment type": "Direct Debit"}}]

    cc = [{"Personal":
               {"Provider": "CommonWealth Bank",
                "ID": "Need Data",
                "contact": "Need Data",
                "payment type": "Blank"},
           "Business":
               {"Provider": "Bank of Melbourne",
                "ID": "Need Data",
                "contact": "Need Data",
                "payment type": "Blank"}}]

    bankac = [{"Personal":
                   {"Provider": "CommonWealth Bank",
                    "ID": "Need Data",
                    "contact": "Need Data",
                    "payment type": "Blank"},
               "Business":
                   {"Provider": "Bank of Melbourne",
                    "ID": "Need Data",
                    "contact": "Need Data",
                    "payment type": "Blank"}}]

    super = [{"Personal":
                  {"Provider": "CommonWealth Bank",
                   "ID": "Need Data",
                   "contact": "Need Data",
                   "payment type": "Blank"}}]

    gov = [{"Personal":
                {"Provider": "CommonWealth Bank",
                 "ID": "Need Data",
                 "contact": "Need Data",
                 "payment type": "Blank"}}]

    savings = [{"Personal":
                    {"Provider": "CommonWealth Bank",
                     "ID": "Need Data",
                     "contact": "Need Data",
                     "payment type": "Blank"},
                "Business":
                    {"Provider": "Bank of Melbourne",
                     "ID": "Need Data", "contact": "Need Data",
                     "payment type": "Blank"}}]

    metals = [{"Gold":
                   {"AMOUNT": "10oz"},
               "Silver":
                   {"AMOUNT": "10oz"},
               "Platinum":
                   {"AMOUNT": "10oz"}}]

    return render_template('main.html', TICKERS=tickers, CURRENCY=currency,
                           POSTCODE=postcode, DAYCOUNT=daycount, UTILITIES=utilities, INSURANCES=insurances,
                           LOANS=loans, CC=cc, BANKAC=bankac, SUPER=super, SAVINGS=savings, METALS=metals,
                           LEGEND=legend, THIRTYMA=thirtyMa, SIXTYMA=sixtyMa, NINETYMA=ninetyMa, TOTALVAL=totalval)




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


@app.route("/domain")
def domain():
    domain = os.environ["REQUEST_URI"]
    print(domain)
    return render_template('chart.html', DOMAIN=domain)


if __name__ == '__main__':
    app.run()

