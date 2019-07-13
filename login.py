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
body
{
	align-self: center;
	background-image:  url('SS1.gif');
	height: 100%;
	width:100%;
	background-repeat: no-repeat;
	background-size: cover;
}
div
{
	background-color: skyblue;
	display: block;
	width:300px
}
</style>

</head>
<body>
        <div>
	<form action="login1.py">
	<table>
	<tr>
	<td colspan="2"><h1 style="font-size: 40px"><center><b>Login Information</b></center></h1></td>
	</tr>
	<tr>
	<td>Username:</td><td><input id="" type="text" name="id"></td>
	</tr>
	<tr>
	<td>Password:</td><td><input type="Password" name="pwd"></td>
	</tr>
	</div>	
	<tr>
		<td><input type="Submit" name=""><input type="Reset" name=""></td><td colspan="2"><a href="reset.py"><button><a href="reset.py">Forget</a></button></a></td>
	</tr>
	</table>
	</form>


	
</body>
</html>''')
