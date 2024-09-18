#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2


# Connect to PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    database="Kymani",
    # Nishi
    # password="12345",
    # port = 5432
    
    # Binh
    password="1234",
    port = 5433
)
cursor = connection.cursor()

# Table: user_account
cursor.execute("""
CREATE TABLE user_account (
    username VARCHAR(45) PRIMARY KEY,
    password VARCHAR(45),
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    email VARCHAR(45),
    project_manager BOOLEAN,
    login_time TIMESTAMP
);
""")

# Table: employee
cursor.execute("""
CREATE TABLE employee (
    employee_code SERIAL PRIMARY KEY,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    user_account VARCHAR(45) REFERENCES user_account(username)
);
""")

# Table: team
cursor.execute("""
CREATE TABLE team (
    team_name VARCHAR(75) PRIMARY KEY
);
""")

# Table: role
cursor.execute("""
CREATE TABLE role (
    role_name VARCHAR(75) PRIMARY KEY
);
""")

# Table: team_member
cursor.execute("""
CREATE TABLE team_member (
    team_name VARCHAR(75) REFERENCES team(team_name),
    employee_code INT REFERENCES employee(employee_code),
    role_name VARCHAR(75) REFERENCES role(role_name),
    PRIMARY KEY (team_name, employee_code)
);
""")

# Table: project_manager
cursor.execute("""
CREATE TABLE project_manager (
    project_id SERIAL PRIMARY KEY,
    user_account VARCHAR(45) REFERENCES user_account(username)
);
""")

# Table: project
cursor.execute("""
CREATE TABLE project (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(75),
    planned_start_date DATE,
    planned_end_date DATE,
    planned_budget DECIMAL,
    spent_budget DECIMAL,
    description TEXT,
    project_manager INT REFERENCES project_manager(project_id)
);
""")

# Table: client_partner
cursor.execute("""
CREATE TABLE client_partner (
    client_name VARCHAR(45) PRIMARY KEY,
    address VARCHAR(75),
    phone_no VARCHAR(15),
    email VARCHAR(45)
);
""")

# Table: on_project
cursor.execute("""
CREATE TABLE on_project (
    client_partner VARCHAR(45) REFERENCES client_partner(client_name),
    project_id INT REFERENCES project(project_id),
    PRIMARY KEY (client_partner, project_id)
);
""")

# Table: activity
cursor.execute("""
CREATE TABLE activity (
    activity_id SERIAL PRIMARY KEY,
    activity_name VARCHAR(75),
    planned_start_date DATE,
    planned_end_date DATE,
    actual_start_date DATE,
    actual_end_date DATE,
    activity_description TEXT,
    project_id INT REFERENCES project(project_id)
);
""")

# Table: task
cursor.execute("""
CREATE TABLE task (
    task_id SERIAL PRIMARY KEY,
    task_name VARCHAR(75),
    planned_start_date DATE,
    planned_end_date DATE,
    actual_start_date DATE,
    actual_end_date DATE,
    task_description TEXT,
    activity_id INT REFERENCES activity(activity_id)
);
""")

# Table: assigned
cursor.execute("""
CREATE TABLE assigned (
    employee_code INT REFERENCES employee(employee_code),
    activity_id INT REFERENCES activity(activity_id),
    PRIMARY KEY (employee_code, activity_id)
);
""")

# Table: preceding_activity
cursor.execute("""
CREATE TABLE preceding_activity (
    preceding_activity_id INT REFERENCES activity(activity_id),
    activity_id INT REFERENCES activity(activity_id),
    PRIMARY KEY (preceding_activity_id, activity_id)
);
""")

# Table: preceding_task
cursor.execute("""
CREATE TABLE preceding_task (
    preceding_task_id INT REFERENCES task(task_id),
    task_id INT REFERENCES task(task_id),
    PRIMARY KEY (preceding_task_id, task_id)
);
""")

connection.commit()
cursor.close()
connection.close()

print("Schema created successfully!")