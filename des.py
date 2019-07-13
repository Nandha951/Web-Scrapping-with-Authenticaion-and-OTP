#!"C:\Program Files (x86)\Python37-32\pythonw.exe"
from urllib.request import *
from urllib.request import *
from xlsxwriter import*
from bs4 import *
import random
import sqlite3
import smtplib
import cgi
print("Content- Type:text/html")
print()
def scrap():
    q=open('avoid.txt','r')
    t=q.read()
    url='https://'+input('url :')
    b=urlopen(url)
    o=BeautifulSoup(b,'html.parser')
    for z in o(['script','style']):
        n=z.extract()
    n=o.get_text()
    n=n.split()
    #n=' '.join(n)
    #print(n)
    y={}
    o={}
    for i in n:
        if i not in o:
            if i not in t:
              x=n.count(i)
              y[i]=x
    #print(y)
    b=sorted(y.items(),key=lambda t:t[1],reverse=True)
    word=[]
    count=[]
    for c in b:
        word.append(c[0])
        count.append(c[1])
    print(word[0],count[0])
    print(word[1],count[1])
    print(word[2],count[2])
    print(word[3],count[3])
    print(word[4],count[4])
    

while(1):
    scrap()
    y=input('continue y/n')
    if y=='y':
        scarp()
    else:
        break
