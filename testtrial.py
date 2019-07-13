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
#print("Content-Type:text/html")
#print()
#q=open('avoid.txt','r')
#t=q.read()
t=['the','₹','of','is','&','to','on','all','you','and','for','Your','your','from','can','in','Online','Shop','Rs.','at','online','have','products','see','Auto...','See','3','with','899.00Rs.','range','-','The','All','inYour']
#form=cgi.FieldStorage()
#url2=form.getvalue('url')
#url="https://"+url2
url='https://www.amazon.in'
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
    a1,a2,a3,a4,a5=str(word[0]),str(word[1]),word[2],word[3],word[4]
    b1,b2,b3,b4,b5=int(count[0]),int(count[1]),int(count[2]),int(count[3]),int(count[4])
    print(a1,b1,a2,b2,a3,b3,a4,b4,a5,b5)
    print("""<!DOCTYPE html>
<html lang="en-US">
<head>
<style>
#piechart
{
width:500px;
height:500px;
position:relative;
left:400px;
}
</style>
</head>
<body>
<input type="text" id="a1" value="%s" style="visibility:hidden">
<input type="text" id="a2" value="%d" style="visibility:hidden">
<input type="text" id="a3" value="%s" style="visibility:hidden">
<input type="text" id="a4" value="%d" style="visibility:hidden">
<input type="text" id="a5" value="%s" style="visibility:hidden">
<input type="text" id="a6" value="%d" style="visibility:hidden">
<input type="text" id="a7" value="%s" style="visibility:hidden">
<input type="text" id="a8" value="%d" style="visibility:hidden">
<input type="text" id="a9" value="%s" style="visibility:hidden">
<input type="text" id="a10" value="%d" style="visibility:hidden">
<!-- <h1 style="text-align:center; color:red;">The Data Scraped from - %s</h1> -->
<div id="piechart">
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
// Draw the chart and set the chart values
function drawChart() {
   var z1=document.getElementById('a1').value;
   var y1=parseInt(document.getElementById('a2').value);
   var z2=document.getElementById('a3').value;
   var y2=parseInt(document.getElementById('a4').value);
   var z3=document.getElementById('a5').value;
   var y3=parseInt(document.getElementById('a6').value);
   var z4=document.getElementById('a7').value;
   var y4=parseInt(document.getElementById('a8').value);
   var z5=document.getElementById('a9').value;
   var y5=parseInt(document.getElementById('a10').value);
  var data = google.visualization.arrayToDataTable([
  ['Words', 'Counts'],
  [z1,y1],
  [z2, y2],
  [z3,y3],
  [z4,y4],
  [z5,y5],
]);

  // Optional; add a title and set the width and height of the chart
  var options = {'title':'', 'width':550, 'height':400};

  // Display the chart inside the <div> element with id="piechart"(pie,area,bar,line)
  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
}
</script>
</div>
</body>
</html>
"""  % (a1,b1,a2,b2,a3,b3,a4,b4,a5,b5))
#print(word[0],count[0])
#print('\n')
#print(word[1],count[1])
#print(word[2],count[2])
#print(word[3],count[3])
#print(word[4],count[4])
#print(word,count)
