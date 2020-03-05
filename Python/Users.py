# Copyright (c)  2020
#Author : jignash reddy


""" Users.py - To add or delete or update or fetch users for login"""

import os
import configparser
import base64

import mysql.connector
from mysql.connector import Error


configfilepath=os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini')
config = configparser.ConfigParser()
config.read(configfilepath)
hostname=config.get('MYSQL','host')
database=config['MYSQL']['database']
sql_user=config['MYSQL']['username']
sql_password=config['MYSQL']['password']


class Usermanagement:
    def adduser(self, usernme, password, email=None):
        try:
            password=base64.b64encode(password.encode('ascii'))
            connection = mysql.connector.connect(host=hostname,
                                                database=database,
                                                user=sql_user,
                                                password=sql_password)

            sql_select_Query = f"INSERT INTO `{database}`.`users` (`username`, `email_id`, `password`) VALUES ('{usernme}', '{email}', '{password.decode('ascii')}')"
            print(sql_select_Query)
            cursor = connection.cursor()
            res=cursor.execute(sql_select_Query)
            connection.commit()
            print(res)
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
        return res
    def deluser():
        pass
    def upduser():
        pass
    def fetchuser():
        pass
    
