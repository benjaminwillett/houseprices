from flask import Flask, render_template
from BeautifulSoup import BeautifulSoup
import urllib3
import time


app = Flask(__name__)

loop = True
priceHistory = []
change = 0
http = urllib3.PoolManager()


while loop == True:
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

    tempChelt = linksChelt[2]
    tempMent = linksMent[2]
    tempPark = linksPark[2]
    tempBeau = linksBeau[2]
    print(str(tempChelt) + "is temp")

    refinedChelt = tempChelt
    refinedMent = tempMent
    refinedPark = tempPark
    refinedBeau = tempBeau
    print(str(refinedChelt) + "is refined")

    priceHistory.append(refinedChelt)
    print(str(priceHistory) + "is price history")

    if refinedChelt > priceHistory[0]:
        change = ((int(refinedChelt) - (int(priceHistory[0]))))
    print(str(change) + " is the change")
    time.sleep(60)


@app.route('/' , methods=['GET','POST'])
def default():
    global refinedChelt
    global refinedMent
    global refinedPark
    global refinedBeau
    global priceHistory
    global change
    return render_template('main.html', REFINEDCHELT=refinedChelt, REFINEDMENT=refinedMent, REFINEDPARK=refinedPark, REFINEDBEAU=refinedBeau, PRICEHISTORY=priceHistory, CHANGE=change)



if __name__ == '__main__':
    app.run()

