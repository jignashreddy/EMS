import mysql.connector
from mysql.connector import Error
import os
import configparser

configfilepath=os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini')
config = configparser.ConfigParser()
config.read(configfilepath)
print (config.sections())
hostname=config.get('MYSQL','host')
database=config['MYSQL']['database']
user=config['MYSQL']['username']
password=config['MYSQL']['password']

try:
    connection = mysql.connector.connect(host=hostname,
                                         database=' ',
                                         user=user,
                                         password=password)

    sql_select_Query = f"CREATE SCHEMA `{database}` "
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    sql_select_Query = f"use `{database}` "
    cursor.execute(sql_select_Query)
    users_table = """CREATE TABLE `users` (
                    `user_id` int(11) NOT NULL AUTO_INCREMENT,
                    `username` varchar(45) DEFAULT NULL,
                    `email_id` varchar(45) DEFAULT NULL,
                    `password` varchar(45) DEFAULT NULL,
                    `status` varchar(45) DEFAULT 'offline',
                    `name` varchar(45) DEFAULT NULL,
                    PRIMARY KEY (`user_id`),
                    UNIQUE KEY `User_id_UNIQUE` (`user_id`),
                    UNIQUE KEY `username_UNIQUE` (`username`),
                    UNIQUE KEY `email_id_UNIQUE` (`email_id`)
                    ) ENGINE=InnoDB AUTO_INCREMENT=1014 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""
    cursor.execute(users_table)

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")