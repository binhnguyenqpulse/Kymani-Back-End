#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 00:01:41 2024

@author: binhnguyen
"""


import psycopg2
import json


# Connect to PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    database="Kymani",
    user="postgres",
    password="12345",
    port = 5432
)
cursor = connection.cursor()

def load_json_data(file_path):
    """Load data from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)
    
def insert_user_accounts(data, conn):
    """Insert user account data into the database."""
    try:
        with conn.cursor() as cursor:
            insert_query = """
                INSERT INTO user_account (username, first_name, last_name, email, project_manager, login_time)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            for user in data:
                cursor.execute(insert_query, (
                    user['username'],
                    user['first_name'],
                    user['last_name'],
                    user['email'],
                    user['project_manager'],
                    user['login_time']
                ))
        conn.commit()
        print("Data inserted successfully.")
    except Exception as e:
        conn.rollback()
        print(f"An error occurred: {e}")


json_file_path = 'user_account_data.json'
user_data = load_json_data(json_file_path)

insert_user_accounts(user_data, connection)
# Insert data into user_account
# cursor.execute("""
# INSERT INTO user_account (username, first_name, last_name, email, project_manager, login_time)
# VALUES
#     ('jdoe', 'John', 'Doe', 'john.doe@example.com', TRUE, '2024-09-01 10:00:00'),
#     ('asmith', 'Alice', 'Smith', 'alice.smith@example.com', FALSE, '2024-09-02 09:30:00');
# """)

# # Insert data into employee
# cursor.execute("""
# INSERT INTO employee (first_name, last_name, user_account)
# VALUES
#     ('John', 'Doe', 'jdoe'),
#     ('Alice', 'Smith', 'asmith');
# """)

# # Insert data into team
# cursor.execute("""
# INSERT INTO team (team_name)
# VALUES
#     ('Engineering'),
#     ('Marketing');
# """)

# # Insert data into role
# cursor.execute("""
# INSERT INTO role (role_name)
# VALUES
#     ('Developer'),
#     ('Manager');
# """)

# # Insert data into team_member
# cursor.execute("""
# INSERT INTO team_member (team_name, employee_code, role_name)
# VALUES
#     ('Engineering', 1, 'Developer'),
#     ('Engineering', 2, 'Manager');
# """)

# # Insert data into project_manager
# cursor.execute("""
# INSERT INTO project_manager (user_account)
# VALUES
#     ('jdoe');
# """)

# # Insert data into project
# cursor.execute("""
# INSERT INTO project (project_name, planned_start_date, planned_end_date, planned_budget, spent_budget, description, project_manager)
# VALUES
#     ('Project Alpha', '2024-09-01', '2025-01-01', 100000, 20000, 'A high-priority engineering project', 1);
# """)

# # Insert data into client_partner
# cursor.execute("""
# INSERT INTO client_partner (client_name, address, phone_no, email)
# VALUES
#     ('TechCorp', '123 Silicon Valley', '555-1234', 'contact@techcorp.com');
# """)

# # Insert data into on_project
# cursor.execute("""
# INSERT INTO on_project (client_partner, project_id)
# VALUES
#     ('TechCorp', 1);
# """)

# # Insert data into activity
# cursor.execute("""
# INSERT INTO activity (activity_name, planned_start_date, planned_end_date, actual_start_date, actual_end_date, activity_description, project_id)
# VALUES
#     ('Planning', '2024-09-01', '2024-09-15', '2024-09-01', '2024-09-14', 'Initial project planning', 1);
# """)

# # Insert data into task
# cursor.execute("""
# INSERT INTO task (task_name, planned_start_date, planned_end_date, actual_start_date, actual_end_date, task_description, activity_id)
# VALUES
#     ('Define Requirements', '2024-09-01', '2024-09-05', '2024-09-01', '2024-09-04', 'Gathering initial requirements', 1);
# """)

# # Insert data into assigned
# cursor.execute("""
# INSERT INTO assigned (employee_code, activity_id)
# VALUES
#     (1, 1),
#     (2, 1);
# """)

# # Insert data into preceding_activity
# cursor.execute("""
# INSERT INTO preceding_activity (preceding_activity_id, activity_id)
# VALUES
#     (1, 1);  -- The same activity precedes itself in this simplified case
# """)

# # Insert data into preceding_task
# cursor.execute("""
# INSERT INTO preceding_task (preceding_task_id, task_id)
# VALUES
#     (1, 1);  -- The same task precedes itself in this simplified case
# """)
cursor.close()
connection.close()
