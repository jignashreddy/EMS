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

    employee_table = """CREATE TABLE `employee_details` (
                        `emp_id` int NOT NULL AUTO_INCREMENT,
                        `emp_name` varchar(45) NOT NULL,
                        `department` varchar(45) DEFAULT NULL,
                        `designation` varchar(45) DEFAULT NULL,
                        `phone_number` varchar(45) NOT NULL,
                        `mail_id` varchar(45) DEFAULT NULL,
                        `address` varchar(45) DEFAULT NULL,
                        `blood_type` varchar(45) DEFAULT NULL,
                        PRIMARY KEY (`emp_id`),
                        UNIQUE KEY `emp_id_UNIQUE` (`emp_id`)
                        ) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""
    cursor.execute(employee_table)

    employee_attendance_table = """CREATE TABLE `employee_attendance` (
                                    `emp_id` int NOT NULL,
                                    `date` date DEFAULT NULL,
                                    `partial_amount` int(11) DEFAULT '0',
                                    `last_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                                    `status` varchar(45) DEFAULT NULL,
                                    PRIMARY KEY (`emp_id`),
                                    CONSTRAINT `emp_id` FOREIGN KEY (`emp_id`) REFERENCES `employee_details` (`emp_id`)
                                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""
    cursor.execute(employee_attendance_table)

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")