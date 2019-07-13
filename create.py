#!"C:\Program Files (x86)\Python37-32\pythonw.exe"
from urllib.request import *
from urllib.request import *
from xlsxwriter import*
from bs4 import *
import random
import sqlite3
import smtplib
print('''
<!DOCTYPE html>
<html>
<head>
    <style type="text/css">
    body
    {
	background-image:  url('giphy.gif');
	height: 100%;
	width:100%;
	background-repeat: no-repeat;
	background-size: cover;
    }
    div
    {
	background-color: grey;
	display: block;
	width: 400px;
    }
    </style>

	
</head>
<body>

<form action="create1.py" method="get">
<div>
	<table>
	<tr>
	<td colspan="2"><h1 style="font-size: 40px"><center><b>Personal Information</b></center></h1></td>
	</tr>
	<tr>
	<td>E-mail:</td><td><input type="text" name="email"></td>
	</tr>
	<tr>
	<td>Username:</td><td><input id="" type="text" name="name"></td>
	</tr>
	<tr>
	<td>Password:</td><td><input type="Password" name="pwd"></td>
	</tr>
	<tr><td>Mobile Number:</td><td><input type="Number" name="no"></td></tr>
	</table>
	</div>
	<tr><td><input type="Submit" name=""></td><input type="Reset" name=""></td>
	</tr>

	</form>

</body>
</html>''')
