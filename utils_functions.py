#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:30:35 2024

@author: binhnguyen
"""
import json

########################################

# Create JSON file

def load_json_data(file_path):
    """Load data from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

########################################

# CRUD ops

# 1. Create
def create_user_account (username,first_name, last_name, email, project_manager, login_time, cursor, connection):
    insert_query = """
    INSERT INTO user_account (username,first_name, last_name, email, project_manager, login_time)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    cursor.execute (insert_query, (username,first_name, last_name, email, project_manager, login_time))
    connection.commit()
    
# 2. Read
def read_user_account (cursor, connection):
    cursor.execute("SELECT * FROM user_account")
    rows = cursor.fetchall()
    for row in rows:
        print (row)
        
# 3. Update
def update_user_email (username, email, cursor, connection):
    update_query = """ 
    UPDATE user_account
    SET email = %s
    WHERE username = %s
    """
    cursor.execute (update_query, (email, username))
    connection.commit()
        
# 4. Delete
def delete_user_account (username, cursor, connection):
    delete_query = """
    DELETE FROM user_account 
    WHERE username = %s
    """
    cursor.execute (delete_query, (username,))
    connection.commit ()
    print(f"User {username} deleted successfully!")


######################################## CRUD 