#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2
from utils_functions import *


# Connect to PostgreSQL database
connection = psycopg2.connect(
    
    host="localhost",
    database="Kymani",
    user="postgres",
    
    # Nishi
    # password="12345",
    # port = 5432
    
    # Binh
    password="1234",
    port = 5433

)
cursor = connection.cursor()

######################################## 

# Loading file
file_path = 'user_account_data.json'

users = load_json_data(file_path)

for user in users:
    # create_user_account (user['username'], user['password'], user['first_name'], user['last_name'], user['email'], user['project_manager'], user['login_time'], cursor, connection)
    update_user_email('binhnguyen','binh.nguyen@qcp.com',cursor, connection)
    # delete_user_account(user['username'],cursor, connection)
read_user_account(cursor, connection)

######################################## 
cursor.close()
connection.close()






