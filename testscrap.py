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
t=['the','a','₹','of','is','&','to','on','all','you','and','for','Your','your','from','can','in','Online','Shop','Rs.','at','online','have','products','see','Auto...','See','3','with','899.00Rs.','range','-','The','All','inYour']
form=cgi.FieldStorage()
url2=form.getvalue('url')
#url2=input()
url="https://"+url2
#url='https://www.amazon.in'
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

b=sorted(y.items(),key=lambda t:t[1],reverse=True)
word=[]
count=[]
for c in b:
    word.append(c[0])
    count.append(c[1])
a1,a2,a3,a4,a5=word[0],word[1],word[2],word[3],word[4]
b1,b2,b3,b4,b5=int(count[0]),int(count[1]),int(count[2]),int(count[3]),int(count[4])
#print(a1,b1,a2,b2,a3,b3,a4,b4,a5,b5)
print('''
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="link.css">
<style type="text/css">
</style>
	<script type="text/javascript" src="RGraph.common.core.js"></script>
	<script type="text/javascript" src="RGraph.bar.js"></script>
</head>
<body style="">
<div id ="a">
<CANVAS width="500" height="250" ID="test" style="border: 2px solid black; background-color:blue"></CANVAS></div>

<script>
	var bar=new RGraph.Bar('test',[%d,%d,%d,%d,%d]);
	bar.Set('chart.colors',['red']);
	bar.Set('chart.title',"SEO Report");
	bar.Set('chart.labels',["%s","%s","%s","%s","%s"]);
	bar.draw();
</script>

<div id="">
	<h3><button><a href="main.py">Home</a></button>
	<button><a href="url.py">Try Again</a></button></h3>
</div>
</body>
</html>''' % (b1,b2,b3,b4,b5,a1,a2,a3,a4,a5))
