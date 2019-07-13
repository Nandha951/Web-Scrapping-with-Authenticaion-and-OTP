#!"C:\Program Files (x86)\Python37-32\pythonw.exe"
from urllib.request import *
from urllib.request import *
from xlsxwriter import*
from bs4 import *
import random
import sqlite3
import smtplib
import cgi
import sys
print("Content-Type: text/html")
print()
t=['the','of','is','&','to','on','all','you','and','for','your','from','can','in','Online','Shop','Rs.','at','online','have','products','see','Auto...','See','3','with','899.00Rs.','range','-','The','All','inYour']
#url=input()
form=cgi.FieldStorage()
url2=form.getvalue("url1")
#url2="www.google.com"
url2=str(url2)
url='https://'+url2
b=urlopen(url)
o=BeautifulSoup(b,'html.parser')
for z in o(['script','style']):
    n=z.extract()
n=o.get_text()
n=n.split()
y={}
o={}
for i in n:
    if i not in o:
        if i not in t:
            x=n.count(i)
            y[i]=x

print(y)
b=sorted(y.items(),key=lambda t:t[1],reverse=True)
word=[]
count=[]
for c in b:
    word.append(c[0])
    count.append(c[1])

print(word,count)

print('''<!DOCTYPE html>
<html>
<head>
<script>
    setTimeout(function()
    {
        window.location.href='graph1.py?a=%s,b=%s'
    },10);
</script>
<body>
</body>
</head>
</html>'''% (word,count))
