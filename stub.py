styleSheet = """
        QPushButton {
            background-color: rgb(153, 158, 158);
            color: black;
            border-radius: 3px;
            border: 2px solid black;
        }
        QPushButton:hover {
            background-color: rgb(202, 204, 204);
            color: black;
            border: 2px solid black;
        }
        QLineEdit {
            border-radius: 3px;
            border: 2px solid grey;
        }
    """

import requests
from bs4 import BeautifulSoup

cost_class = "_30jeq3 _16Jk6d"
star_class = "_3LWZlK"
title_class = "B_NuCI"

def get_cost(x):
    try:
        req = requests.get(x)
        soup = BeautifulSoup(req.content, 'html.parser')
        cost = soup.find('div', class_=cost_class).text
        return cost
    except:
        pass

def get_star(x):
    try:
        req = requests.get(x)
        soup = BeautifulSoup(req.content, 'html.parser')
        star = soup.find('div', class_=star_class).text
        return star
    except:
        pass

def get_title(x):
    try:
        req = requests.get(x)
        soup = BeautifulSoup(req.content, 'html.parser')
        title = soup.find('span', class_=title_class).text
        return title
    except:
        pass