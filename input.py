import os
import requests

def create(x):
    with open("creds.txt", 'w') as fl:
        fl.write(x[0] +' ')
        fl.write(x[1])

def createDetails(x):
    with open("creds.txt", 'a') as fl:
        fl.write('\n')
        for i in x:
            if ( i != x[len(x)-1] ):
                fl.write(i + ' ')
            else:
                fl.write(i)
        fl.write('\n')
        

def verify(x):
    with open("creds.txt", 'r') as fl:
        det = fl.read().split()
        for i, j in zip(x, det):
            if ( i != j):
                return False
        if (len(det)):
            return True
    
def addLink(x):
    req = requests.get(x)
    if ( req.status_code == 200 ):
        with open("creds.txt", 'a') as fl:
            fl.write( x + '\n')
        
def getLinks():
    with open("creds.txt", 'r') as fl:
        x = []
        for i in fl.readlines():
            x.append(i.strip())
    return x[2:]


def getLink(x):
    with open("creds.txt", 'r') as fl:
        content = fl.readlines()
        try:
            return content[x]
        except:
            pass


def delLink(x):
    with open("creds.txt", 'r') as fl:
        content = fl.readlines()
        try:
            del content[x]
        except:
            pass
    with open("creds.txt", 'w') as fl:
        fl.writelines(content)

def getDetals():
    with open("creds.txt", 'r') as fl:
        res = fl.readlines()
        if ( len(res) > 0 ):
            return [1].split() 

def order(x):
    os.system("pythonw order.py {} {} {} {} {} {} {}".format(x[0], x[1], x[2], x[3], x[4], x[5], x[6]))

