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
id=form.getvalue('id')
pwd=form.getvalue('pwd')
a=sqlite3.connect('auth.db')
b=a.execute('select * from auth')
for z in b:
    print()
if(z[2]==id and z[3]==pwd):
    print('''
    <!DOCTYPE html>
    <html>
    <head>
    <style type="text/css">
    body
    {
    align-self: center;
	background-image:  url('h.gif');
	height: 100%;
	width:100%;
	background-repeat: no-repeat;
	background-size: cover;
    }
    div
    {
	background-color: white;
	display: inline;
    }
</style>

	<title></title>
    </head>
    <body>
    <div align="center">
	<h1 style="align-items: center; color: green">Login Success</h1>
	<h3><button><a href="main.py">Home</a></button>
	<h3><button><a href="url.py">SEO</a></button></h3>
	</div>
    </body>
    </html>''')
else:
    print('''<!DOCTYPE html>
    <html>
    <head>
        <title></title>
    </head>
    <body>
	<h1>Login Failure</h1>
	<a href="main.py">Home</a>
    </body>
    </html>''')
