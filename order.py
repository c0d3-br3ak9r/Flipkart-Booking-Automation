import sys
import time
import flipkart
import datetime as dt
import requests
from bs4 import BeautifulSoup

x = sys.argv[1:]
x[5] = x[5] + ' ' + x[6]
del x[6]

while True:
    req = requests.get(x[6])
    soup = BeautifulSoup(req.content, 'html.parser')
    stock = soup.find('button', class_="_2KpZ6l _2U9uOA ihZ75k _3AWRsL").text
    if ( ( stock == ' BUY NOW' ) and ( str(dt.datetime.now()) >= x[5] ) ):
        flipkart.automate(x)
        break
    time.sleep(5)