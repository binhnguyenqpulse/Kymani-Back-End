#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Interacting with DB of Kymani using psycopg2

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

# create_user_account ('binhnguyen','1234','binh@qcp.com', cursor, connection)
# update_user_email('binhnguyen','binh.nguyen@qcp.com',cursor, connection)
# delete_user_account('binhnguyen',cursor, connection)
read_user_account(cursor, connection)

######################################## 

cursor.close()
connection.close()
print("Execution successful!")
