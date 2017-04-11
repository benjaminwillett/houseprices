from flask import Flask, render_template
from BeautifulSoup import BeautifulSoup
import urllib3


app = Flask(__name__)

priceHistory = []
http = urllib3.PoolManager()
url = http.request("GET", "https://www.realestate.com.au/neighbourhoods/cheltenham-3192-vic", preload_content=False)

soup = BeautifulSoup(url)

links = soup.findAll("div", {"class": "price strong"})
temp = links[2]
print(str(temp) + "is temp")
refined = temp
print(str(refined) + "is refined")

priceHistory.append(refined)
print(str(priceHistory) + "is price history")

if refined > priceHistory[0]:
    change = ((int(refined) - (int(priceHistory[0]))))


@app.route('/' , methods=['GET','POST'])
def default():
    global links
    global soup
    global refined
    global priceHistory
    global change
    return render_template('main.html', LINKS=links, REFINED=refined, PRICEHISTORY=priceHistory, CHANGE=change)



if __name__ == '__main__':
    app.run()

