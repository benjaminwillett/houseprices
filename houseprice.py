from flask import Flask
import requests
from lxml import html

r = requests.get("https://www.realestate.com.au/neighbourhoods/cheltenham-3192-vic")
tree = html.fromstring(r.content)

prices = tree.xpath('//*[@id="median-price"]/div[2]/div/div[1]/div[1]/div[1]/a[3]/div[2]')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Medium House Price Cheltenham!'


if __name__ == '__main__':
    app.run()

