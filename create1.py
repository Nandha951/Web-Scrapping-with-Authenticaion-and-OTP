#!"C:\Program Files (x86)\Python37-32\pythonw.exe"
from urllib.request import *
from xlsxwriter import*
from bs4 import *
import random
import sqlite3
import smtplib
import cgi
a=sqlite3.connect('auth.db')
#a.execute('drop table auth')
#a.execute('create table auth (id int,email varchar(100),username varchar(100),password varchar(100),no varchar(12));')
#a.execute('insert into auth (id,email,username,password,no)values(1,"admin","admin","admin","admin")');
#a.commit()
b=a.execute('select * from auth')
for z in b:
    print()
form=cgi.FieldStorage()
mail=form.getvalue('email')
name=form.getvalue('name')
pwd=form.getvalue('pwd')
num=form.getvalue('no')
a.execute(('update auth set email=?,username=?,password=?,no=? where id=1'),(mail,name,pwd,num))
a.commit()
print('''
<!DOCTYPE html>
<html>
<head>
<style type="text/css">
body
{
	background-image:  url('d.gif');
	height: 100%;
	width:100%;
	background-repeat: no-repeat;
	background-size: cover;
}
div
{
        
	background-color: white;
	display: inline;
	width:300px
}
</style>


	<title></title>
</head>
<body>
        <div align="center">
	<h1 style="color:yellow">Creation Success</h1>
	<h3><button><a href="main.py">Home</a>
	<button><a href="login.py">Login</a></button</h3>
	</div>
</body>
</html>''')
