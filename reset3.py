#!"C:\Program Files (x86)\Python37-32\pythonw.exe"
from urllib.request import *
from urllib.request import *
from xlsxwriter import*
from bs4 import *
import random
import sqlite3
import smtplib
import cgi
form=cgi.FieldStorage()
otp=form.getvalue('otp')
a=sqlite3.connect('otp.db')
#a.execute('create table otp (id int,otp varchar(5))')
#a.execute('insert into otp (id,otp)values(1,"admin")');
a.execute('update otp set otp=? where id=1',[otp])
a.commit()
b=a.execute('select * from otp')
for z in b:
    print()
if (z[1]==otp):
    print('''
    <!DOCTYPE html>
    <html>
    <head>
    <style type="text/css">
    	#a
    	{
    	font-size: 30px
    	}
    </style>
	<title></title>
    </head>
    <body style="background-image: url('g3.gif');">
	<form action="reset4.py">
	<div align="center">
	<h1 style="color: lightblue">Reset in Process</h1>
	<table>
	<tr>
	<td><div id="a" style="color:red;">New Password:</div><input type="text" name="npwd"></td>
	</tr>
	<tr>
	<td align="center"><input type="Submit" name=""></td>
	</tr>
	</table>
	</div>
	</form>
    </body>
    </html> ''')
else:
    print('''
    <!DOCTYPE html>
    <html>
    <head>
	<title></title>
    </head>
    <body>
	<h1>Reset Success</h1>
    </body>
    </html>''')
