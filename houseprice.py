from flask import Flask
from BeautifulSoup import BeautifulSoup
import urllib3

http = urllib3.PoolManager()
url = http.request("GET", "https://www.realestate.com.au/neighbourhoods/cheltenham-3192-vic")
content = url.read()

soup = BeautifulSoup(content)

links = soup.findAll('//*[@id="median-price"]/div[2]/div/div[1]/div[1]/div[1]/a[3]/div[2]')


app = Flask(__name__)

@app.route('/')
def hello_world():
    global links
    return '4 Bed Medium House Price Cheltenham =', links


if __name__ == '__main__':
    app.run()

