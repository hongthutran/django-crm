# Install Mysql on your computer
# https://dev.mysql.com/dowloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

dataBase = mysql.connector.connect(
	host = os.getenv("DB_HOST"),
	user = os.getenv("DB_USER"),
	passwd = os.getenv("DB_PASSWORD"),
	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE crm_django_db")

print("All done!")

