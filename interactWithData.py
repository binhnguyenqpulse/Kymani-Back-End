#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:00:27 2024

@author: binhnguyen
"""

# Interacting with DB of Kymani using psycopg2

import psycopg2


# Connect to PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    database="Kymani",
    user="postgres",
    password="1234",
    port = 5433
)
cursor = connection.cursor()
########################################

# Let's do a CURD command so we can practice 

# 1. Create
def create_user_account (username, password, email):
    insert_query = """
    INSERT INTO user_account (username, password, email)
    VALUES (%s,%s,%s)
    """
    cursor.execute (insert_query, (username, password, email))
    connection.commit()
    
# 2. Read
def read_user_account ():
    cursor.execute("SELECT * FROM user_account")
    rows = cursor.fetchall()
    for row in rows:
        print (row)
        
# 3. Update
def update_user_email (username, email):
    update_query = """ 
    UPDATE user_account
    SET email = %s
    WHERE username = %s
    """
    cursor.execute (update_query, (email, username))
    connection.commit()
        
# 4. Delete
def delete_user_account (username):
    delete_query = """
    DELETE FROM user_account 
    WHERE username = %s
    """
    cursor.execute (delete_query, (username,))
    connection.commit ()
    print(f"User {username} deleted successfully!")


######################################## CRUD 
create_user_account ('binhnguyen','1234','binh@qcp.com')
update_user_email('binhnguyen','binh.nguyen@qcp.com')
# delete_user_account('binhnguyen')
read_user_account()


######################################## Display team member
# cursor.execute("""SELECT * FROM team_member;""")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# connection.commit()

# cursor.execute("""SELECT * FROM project_manager;""")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# connection.commit()

######################################## 
cursor.close()
connection.close()
print("Execution successful!")
