from flask import Flask, render_template, Response, redirect, url_for, request, session, abort
from BeautifulSoup import BeautifulSoup
from datetime import datetime
import urllib
import urllib3
import threading
import json
import os
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user


def getcontent():

    realestateurl = "https://www.realestate.com.au/neighbourhoods/"
    postcode = [{"3192": {"price": "100000", "suburb": "cheltenham"},
                     "3193": {"price": "100000", "suburb": "beaumaris"},
                     "3195": {"price": "500000", "suburb": "parkdale"},
                     "3194": {"price": "777777", "suburb": "mentone"}}]

    for item in postcode:
        for each in item:
            priceurl = request("GET", realestateurl + item[each]["suburb"] + "-" + (str(each)) + "-vic", preload_content=False)
            soup = BeautifulSoup(priceurl)
            links = soup.findAll("div", {"class": "price strong"})
            print links
            postcode[0][each]["price"] = links[2]
            string = postcode[0][each]["price"]
            try:
                blah = (str(string))
                newblah = blah.replace('<div class="price strong">$', "$")
                finalblah = newblah.replace('</div>', "")
                postcode[0][each]["price"] = finalblah
            except:
                postcode[0][each]["price"] = "No DATA!"

getcontent()

