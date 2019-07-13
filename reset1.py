#!"C:\Program Files (x86)\Python37-32\pythonw.exe"
from urllib.request import *
from urllib.request import *
from xlsxwriter import*
from bs4 import *
import random
import sqlite3
import smtplib
import cgi
a=sqlite3.connect('auth.db')
b=a.execute('select * from auth')
for z in b:
    print()
form=cgi.FieldStorage()
no=form.getvalue('num')
if (z[4]=='7598707700'):
    email=z[1]
    otp=''
    alpha=[]
    for r in range(48,123):
        if (r in range(91,97)):
            continue
        if (r in range(58,65)):
            continue
        alpha.append(chr(r))
    for y in range(5):
        otp+=str(random.choice(alpha))
    #print(otp)
    msg='The One Time Password(OTP) is '+otp
    #print(msg)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    a=sqlite3.connect('otp.db')
    #a.execute('create table otp (id int,otp varchar(5))')
    #a.execute('insert into otp (id,otp)values(1,"admin")');
    a.execute(('update otp set otp=? where id=1'),[otp])
    a.commit()
    server.login('damondharan@gmail.com','ddaammoo')
    server.sendmail('damondharan@gmail.com',email,msg)
    print('''
<!DOCTYPE html>
    <html>
    <head>
    <style>
    body
    {
	height: 100%;
	width:100%;
	background-repeat: no-repeat;
	background-size: cover;
    }
    </style>
	<title></title>
    </head>
    <body style="background-image: url('g4.gif');">
   	<div align="center">
	<h1 style="color: lightblue">OTP sent</h1>
	<button><h3><a href="reset2.py">Verify</a></h3></button>
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
    <h1>Reset failure</h1>
    </body>
    </html>''')
