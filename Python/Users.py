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
    def __init__(self):
        self.connection = mysql.connector.connect(host=hostname,
                                    database=database,
                                    user=sql_user,
                                    password=sql_password)


    def adduser(self, usernme, name, upassword, email=None):
        try:
            u_password=base64.b64encode(upassword.encode('ascii'))
            cursor = self.connection.cursor()
            user_add_Query = f"INSERT INTO `{database}`.`users` (`username`, `name`, `email_id`, `password`) VALUES ('{usernme}', '{name}', '{email}', '{u_password.decode('ascii')}')"
            print(user_add_Query)
            cursor.execute(user_add_Query)
            self.connection.commit()
            res = "User record inserted successfully"
        except Error as e:
            print("Error reading data from MySQL table", e)
            res = "User not inserted"
        finally:
            if (self.connection.is_connected()):
                self.connection.close()
                cursor.close()
        return res

    def deluser(self,username):
        try:
            cursor = self.connection.cursor()
            delete_add_Query = f"DELETE FROM `{database}`.`users` WHERE (`username` = '{username}')"
            print(delete_add_Query)
            cursor.execute(delete_add_Query)
            self.connection.commit()
            res = "User record deleted successfully"
        except Error as e:
            print("Error reading data from MySQL table", e)
            res = "User not deleted"
        finally:
            if (self.connection.is_connected()):
                self.connection.close()
                cursor.close()
        return res


    def upduser(self,username,name=None,email_id=None):
        try:
            cursor = self.connection.cursor()
            update_add_Query = f"UPDATE `{database}`.`users` SET `email_id` = '{email_id}',`name`='{name}' WHERE (`username` = '{username}')"
            print(update_add_Query)
            cursor.execute(update_add_Query)
            self.connection.commit()
            res = "User record updated successfully"
        except Error as e:
            print("Error reading data from MySQL table", e)
            res = "User not updated"
        finally:
            if (self.connection.is_connected()):
                self.connection.close()
                cursor.close()
        return res

    def validateuser(self,userentry):
        try:
            cursor = self.connection.cursor()
            check_user_Query = f"SELECT * FROM `{database}`.`users` WHERE (`username` = '{userentry}' OR `email_id` = '{userentry}')"
            print(check_user_Query)
            cursor.execute(check_user_Query)
            result = cursor.fetchall()
            if(result):
                res = "User record found successfully"
                response=True
            else:
                res = "No such record Found"
                response=False
        except Error as e:
            print("Error reading data from MySQL table", e)
            response = ("Exception raised",e)

        finally:
            if (self.connection.is_connected()):
                self.connection.close()
                cursor.close()
        return response

    def validatepassword(self,userentry=None,password=None):
        try:
            cursor = self.connection.cursor()
            check_user_pass = f"SELECT `password` FROM `{database}`.`users` WHERE (`username` = '{userentry}' OR `email_id` = '{userentry}')"
            print(check_user_pass)
            cursor.execute(check_user_pass)
            passy = cursor.fetchall()[0][0]
            pasy = base64.b64decode(passy.encode('ascii'))
            if(password==pasy.decode('ascii')):
                res = "User record updated successfully"
                response=True
            else:
                res = "No such record Found"
                response=False
        except Error as e:
            print("Error reading data from MySQL table", e)
            response = ("Exception raised",e)

        finally:
            if (self.connection.is_connected()):
                self.connection.close()
                cursor.close()
        return response
    
