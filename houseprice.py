from flask import Flask, render_template
from BeautifulSoup import BeautifulSoup
import urllib3

app = Flask(__name__)

http = urllib3.PoolManager()
url = http.request("GET", "https://www.realestate.com.au/neighbourhoods/cheltenham-3192-vic", preload_content=False)
#content = url.read()
print(url)
soup = BeautifulSoup(url)
print(soup)

links = soup.findAll('//*[@id="median-price"]/div[2]/div/div[1]/div[1]/div[1]/a[3]/div[2]')
print(links)


@app.route('/' , methods=['GET','POST'])
def default():
    global links
    global soup
    return render_template('main.html', LINKS=links, SOUP=soup)



if __name__ == '__main__':
    app.run()

