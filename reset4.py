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
npwd=form.getvalue('npwd')
a=sqlite3.connect('auth.db')
#a.execute('drop table auth')
#a.execute('create table auth (id int,email varchar(100),username varchar(100),password varchar(100),no varchar(12));')
#a.execute('insert into auth (id,email,username,password,no)values(1,"admin","admin","admin","admin")');
a.execute(('update auth set password=? where id=1'),[npwd])
a.commit()
print('''
<!DOCTYPE html>
<html>
<head>

	<title></title>
</head>
<body style="background-image:  url('an.gif');background-repeat: no-repeat;background-size: cover;">
<h1>Reset Success</h1>
<a href="main.py">Home</a>
<a href="login.py">Login</a>
</body>
</html>
''')
