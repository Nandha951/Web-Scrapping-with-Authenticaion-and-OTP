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
form=cgi.FieldStorage()
u1=form.getvalue("a")

u2=form.getvalue("b")
print(u1,u2)
print('''
<!DOCTYPE html>
<html>
<head>
	<script type="text/javascript" src="RGraph.common.core.js"></script>
	<script type="text/javascript" src="RGraph.bar.js"></script>
</head>
<body>
	<CANVAS width="500" height="250" ID="test" style="border: 2px solid black"></CANVAS>
<script>

	var bar=new RGraph.Bar('test',[b[0],b[1],b[2],b[3]);
	bar.Set('chart.colors',['red']);
	bar.Set('chart.title',"report");
	bar.Set('chart.labels',[a[0],a[1],a[2],a[3]]);
	bar.draw();

</script>
</body>
</html>'''%(u1[0],u2[0]))
