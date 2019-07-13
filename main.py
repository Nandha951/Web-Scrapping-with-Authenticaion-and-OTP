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

print('''
<!DOCTYPE html>
<html>
<head>
<style type="text/css">
div
{
	background-color: white;
	display: inline;
}
body
{
	background-image:  url('200 (1).gif');
	height: 100%;
	width:100%;
	background-repeat: no-repeat;
	background-size: cover;
}
</style>
	<title>Webscraping</title>
</head>
<body>
<div align="center">
	<h1 style="color: red">Welcome to the Computing World</h1>
	<h3>
	<button><a href="main.py">Home</a></button>
	<button><a href="about.py">About us</a></button>
	<button><a href="login.py">Login</a></button>
	<button><a href="create.py">New user</a></button></h3>
</div>
</body>
</html>''')
