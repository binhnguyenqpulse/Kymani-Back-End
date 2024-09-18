#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:51:47 2024

@author: binhnguyen
"""

# Please do the following
# - Create new branch 
# git branch 'name of branch'
# git checkout 'name of branch'
# git pull
# - create a import json file in the utils function
# - import the json file here
# - apply crud to it and adjust the functions accordingly in the utils functions
# - test case of missing data (should we have missing data or should we not have missing data?)


# Example
# x = json(input)
# create_user_account (x.....x....) but make sure this fits the schema of our code

import psycopg2
from utils_functions import *


# Connect to PostgreSQL database
connection = psycopg2.connect(
    
    host="localhost",
    database="Kymani",
    user="postgres",
    password="12345",
    port = 5432
)
cursor = connection.cursor()

# loading file
file_path = 'user_account_data.json'
users = load_json_data(file_path)
for user in users:
    create_user_account (user['username'], user['first_name'], user['last_name'], user['email'], user['project_manager'], user['login_time'], cursor, connection)
    # update_user_email('binhnguyen','binh.nguyen@qcp.com',cursor, connection)
    # delete_user_account(user['username'],cursor, connection)
# read_user_account(cursor, connection)

cursor.close()
connection.close()






