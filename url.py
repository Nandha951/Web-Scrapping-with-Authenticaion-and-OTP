#!"C:\Program Files (x86)\Python37-32\pythonw.exe"
from urllib.request import *
from urllib.request import *
from xlsxwriter import*
from bs4 import *
import random
import sqlite3
import smtplib
import cgi
print('''
<!DOCTYPE html>
<html>
<head>
    <style type="text/css">
    body
    {
	background-image:  url('91.gif');
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
	<form action="testscrap.py">
	<table>
	<tr>
	<td style="font-size: 20px;color: lightpink">URL:<input type="" name="url"></td>
	<td><input type="submit" name=""></td>
	</tr>
	</table>
	</form>
	</div>
</body>
</html>''')
