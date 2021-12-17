from flask import Flask, render_template, Response, redirect, url_for, request, session, abort
from bs4 import BeautifulSoup
from datetime import datetime
import urllib3
import threading
import json
import os
from colours import colour
from lxml import etree


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

    realestateurl = "https://domain.com.au/suburb-profile/"
    postcode = [{"3192": {"twobedprice": "100000", "threebedprice": "100000", "fourbedprice": "100000",
                          "suburb": "cheltenham", "twobedentry": "10000", "twobedhighend": "10000"},
                 "3193": {"twobedprice": "100000", "threebedprice": "100000", "fourbedprice": "100000",
                          "suburb": "beaumaris", "twobedentry": "10000", "twobedhighend": "10000"},
                 "3195": {"twobedprice": "100000", "threebedprice": "100000", "fourbedprice": "100000",
                          "suburb": "parkdale", "twobedentry": "10000", "twobedhighend": "10000"},
                 "3194": {"twobedprice": "100000", "threebedprice": "100000", "fourbedprice": "100000",
                          "suburb": "mentone", "twobedentry": "10000", "twobedhighend": "10000"}}]

    print "This is the postcode"
    print postcode

    for item in postcode:
        print "This is the item"
        print item
        for each in item:
            print "This is each"
            print each
            priceurl = http.request("GET", realestateurl +
                                    item[each]["suburb"] + "-vic" + "-" + (str(each)) , preload_content=False)
            print "This is priceurl"
            print(priceurl)
            soup = BeautifulSoup(priceurl)
            print "This is soup"
            # print(soup)
            dom = etree.HTML(str(soup))
            twobed = dom.xpath('//*[@id="trends"]/div/div/div[2]/table/tbody[1]/tr/td[3]')
            threebed = dom.xpath('//*[@id="trends"]/div/div/div[2]/table/tbody[2]/tr/td[3]')
            fourbed = dom.xpath('//*[@id="trends"]/div/div/div[2]/table/tbody[3]/tr/td[3]')
            twobedentry = dom.xpath('//*[@id="trends"]/div/div/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/div/div/div[1]/div[2]/div')
            twobedhighend = dom.xpath('//*[@id="trends"]/div/div/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/div/div/div[1]/div[3]/div')
            #entry = dom.xpath('//*[@id="trends"]/div/div/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[
            # 1]/div/div/div[1]/div[2]/div')
            #highend = dom.xpath('//*[@id="trends"]/div/div/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[
            # 1]/div/div/div[1]/div[3]/div')
            # print(fourbed)
            print "This is after soup"
            print postcode[0][each]["fourbedprice"]
            try:
                postcode[0][each]["twobedprice"] = twobed[0].text
                postcode[0][each]["threebedprice"] = threebed[0].text
                postcode[0][each]["fourbedprice"] = fourbed[0].text
                postcode[0][each]["twobedentry"] = twobedentry[0].text
                postcode[0][each]["twobedhighend"] = twobedhighend[0].text
                string = postcode[0][each]["fourbedprice"]
                print(string)
            except:
                postcode[0][each]["twobedprice"] = "No DATA!"
                postcode[0][each]["threebedprice"] = "No DATA!"
                postcode[0][each]["fourbedprice"] = "No DATA!"
                postcode[0][each]["twobedentry"] = "No DATA!"
                postcode[0][each]["twobedhighend"] = "No DATA!"
            print("Finished collecting all the content mother fuckers!")
    print(postcode)


def letsthread():
    thread1 = myThread(1, "Thread-1", 1)
    # Start new Threads
    thread1.start()


letsthread()


@app.route('/', methods=['GET', 'POST'])
def default():
    letsthread()
    print colour.green("Loading bittick on Route")
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
                      "quantity": 0.11,
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
                 "BTC-STRAX":
                     {"pair": "BTC",
                      "colour": "rgba(255, 0, 127, 1)",
                      "Last": 0,
                      "url": "STRAX",
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

    print colour.blue("loaded tickers dictionary on Route")

    for each in tickers[0]:

        response = http.request("GET", bittick + each)
        print colour.purple(response)
        usddict = json.loads(response.data.decode('utf-8'))
        print colour.purple(usddict)
        usdmain = usddict['result']
        print colour.purple(usdmain)
        usdlastclean = usdmain
        print colour.purple(usdlastclean)
        usdlast = (float(usdlastclean['Last']))
        print colour.purple(usdlast)
        tickers[0][each]["Last"] = (str(usdlast))

    print colour.green("loading fixer on Route")
    fixer = os.environ.get('FIXER_URL_APIKEY')
    currency = {'USD': 0, 'GBP': 0, 'EUR': 0, 'AUD': 0, }
    print colour.yellow("Currency loaded!")

    responsefixer = http.request("GET", fixer)
    print colour.blue(responsefixer)
    usddictfixer = json.loads(responsefixer.data.decode('utf-8'))
    print colour.blue(usddictfixer)
    usdmainfixer = usddictfixer['rates']
    print colour.blue(usdmainfixer)
    currencyCount = 0

    for each in currency:
        try:
            print "Start of Currency Loop Count " + (str(currencyCount))
            usdratefixer = usdmainfixer[each]
            print colour.blue(usdratefixer)
            currency[each] = (str(usdratefixer))
            print colour.blue(currency[each])
        except:
            currency[each] = "No Data"
        print "End of Currency Loop Count " + (str(currencyCount))
        currencyCount += 1

    print colour.yellow("Currency loop has completed")
    realestateurl = "https://domain.com.au/suburb-profile/"
    postcode = [{"3192": {"twobedprice": "100000", "threebedprice": "100000", "fourbedprice": "100000",
                          "suburb": "cheltenham", "twobedentry": "10000", "twobedhighend": "10000"},
                 "3193": {"twobedprice": "100000", "threebedprice": "100000", "fourbedprice": "100000",
                          "suburb": "beaumaris", "twobedentry": "10000", "twobedhighend": "10000"},
                 "3195": {"twobedprice": "100000", "threebedprice": "100000", "fourbedprice": "100000",
                          "suburb": "parkdale", "twobedentry": "10000", "twobedhighend": "10000"},
                 "3194": {"twobedprice": "100000", "threebedprice": "100000", "fourbedprice": "100000",
                          "suburb": "mentone", "twobedentry": "10000", "twobedhighend": "10000"}}]

    print colour.green("About to Loop through items in POSTCODE")
    itemCount = 0
    for item in postcode:
        for each in item:
            priceurl = http.request("GET", realestateurl + item[each]["suburb"] + "-vic" + "-" + (str(each)),
                                    preload_content=False)
            soup = BeautifulSoup(priceurl)
            dom = etree.HTML(str(soup))
            twobed = dom.xpath('//*[@id="trends"]/div/div/div[2]/table/tbody[1]/tr/td[3]')
            threebed = dom.xpath('//*[@id="trends"]/div/div/div[2]/table/tbody[2]/tr/td[3]')
            fourbed = dom.xpath('//*[@id="trends"]/div/div/div[2]/table/tbody[3]/tr/td[3]')
            twobedentry = dom.xpath('//*[@id="trends"]/div/div/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/div/div/div[1]/div[2]/div')
            twobedhighend = dom.xpath('//*[@id="trends"]/div/div/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/div/div/div[1]/div[3]/div')

            try:
                postcode[0][each]["twobedprice"] = twobed[0].text
                postcode[0][each]["threebedprice"] = threebed[0].text
                postcode[0][each]["fourbedprice"] = fourbed[0].text
                postcode[0][each]["twobedentry"] = twobedentry[0].text
                postcode[0][each]["twobedhighend"] = twobedhighend[0].text
                string = postcode[0][each]["fourbedprice"]
                print(string)
            except:
                postcode[0][each]["twobedprice"] = "No DATA!"
                postcode[0][each]["threebedprice"] = "No DATA!"
                postcode[0][each]["fourbedprice"] = "No DATA!"
                postcode[0][each]["twobedentry"] = "No DATA!"
                postcode[0][each]["twobedhighend"] = "No DATA!"
        itemCount += 1
        print colour.yellow("route item count finishing " + (str(itemCount)))

    legend = "Price"
    print colour.red("Tickers")
    keyCount = 0
    for key in tickers[0]:
        print colour.red("Looping through tickers " + (str(keyCount)))
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
        keyCount += 1
        print colour.red("Finished keyCount loop " + (str(keyCount)))

    for each in tickers[0]:
        lastHol = tickers[0][each]["Last"]
        quantity = tickers[0][each]["quantity"]
        print(str(type(lastHol)) + " is " + each + " " + (str(lastHol)))
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
        print(str(totalval) + " is the totalval of BTC")

    totaldollar = round(float(totalval) * (float(tickers[0]["USDT-BTC"]["Last"])))
    print("$" + str(totaldollar) + " is the totaldollar value")
    print(str(currency["USD"]) + " is exchange rate")
    conversion = (float(2) - (float(currency["USD"])))
    print(str(conversion) + " is the conversion rate")
    austotal = str(round(totaldollar * conversion))

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
                   "ID": "Need Data",
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
                           LEGEND=legend, THIRTYMA=thirtyMa, SIXTYMA=sixtyMa, NINETYMA=ninetyMa, TOTALVAL=totalval,
                           TOTALDOLLAR=totaldollar, AUSTOTAL=austotal)


@app.route('/index_one', methods=['GET', 'POST'])
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


@app.route("/video")
def video():
    return render_template('video/video.html')


@app.route("/d3")
def d3():
    return render_template('d3/d3.html')


@app.route("/anime")
def anime():
    return render_template('anime/anime.html')


@app.route("/granim")
def granim():
    return render_template('granim/granim.html')


@app.route("/scrollreveal")
def scrollreveal():
    return render_template('scrollreveal/scrollreveal.html')


@app.route("/turntable")
def turntable():
    return render_template('turntable/turntable.html')


@app.route("/microlight")
def microlight():
    return render_template('microlight/microlight.html')


@app.route("/choreographer")
def choreographer():
    return render_template('choreographer/choreographer.html')


@app.route("/leaflet")
def leaflet():
    return render_template('leaflet/leaflet.html')


@app.route("/shave")
def shave():
    return render_template('shave/shave.html')


@app.route("/tabulator")
def tabulator():
    return render_template('tabulator/tabulator.html')


@app.route("/baguettebox")
def baguettebox():
    return render_template('baguettebox/baguettebox.html')


@app.route("/bricks")
def bricks():
    return render_template('bricks/bricks.html')


@app.route("/philter")
def philter():
    return render_template('philter/philter.html')


@app.route("/imageblurr")
def imageblurr():
    return render_template('imageblurr/imageblurr.html')


@app.route("/force")
def force():
    return render_template('force/force.html')


@app.route("/velocity")
def velocity():
    return render_template('velocity/velocity.html')


@app.route("/algoliaplaces")
def algoliaplaces():
    return render_template('algoliaplaces/algoliaplaces.html')


@app.route("/izimodal")
def izimodal():
    return render_template('izimodal/izimodal.html')


@app.route("/multiply")
def multiply():
    return render_template('multiply/multiply.html')


@app.route("/flatpicker")
def flatpicker():
    return render_template('flatpicker/flatpicker.html')


@app.route("/sidebars")
def sidebars():
    return render_template('sidebars/sidebars.html')


@app.route("/cleave")
def cleave():
    return render_template('cleave/cleave.html')


@app.route("/skipper")
def skipper():
    return render_template('skipper/skipper.html')


@app.route("/lightgallery")
def lightgallery():
    return render_template('lightgallery/lightgallery.html')


if __name__ == '__main__':
    app.run(debug=True)

