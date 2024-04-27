import mysql.connector

# Establish a single database connection
def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="14thmarch",
        database="employstatusdb"
    )

# Create the Employees table if it doesn't exist
def create_table():
    db_connection = get_database_connection()
    cursor = db_connection.cursor()
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS Employees (id VARCHAR(255) PRIMARY KEY, name TEXT, role TEXT, gender TEXT, status TEXT)")
        db_connection.commit()
    finally:
        cursor.close()
        db_connection.close()

# Fetch all employees from the database
def fetch_employees():
    db_connection = get_database_connection()
    cursor = db_connection.cursor()
    try:
        cursor.execute("SELECT * FROM Employees")
        return cursor.fetchall()
    finally:
        cursor.close()
        db_connection.close()

# Insert a new employee into the database
def insert_employee(id, name, role, gender, status):
    db_connection = get_database_connection()
    cursor = db_connection.cursor()
    try:
        query = "INSERT INTO Employees (id, name, role, gender, status) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (id, name, role, gender, status))
        db_connection.commit()
    finally:
        cursor.close()
        db_connection.close()

# Delete old employee from the database
def delete_employee(id):
    db_connection = get_database_connection()
    cursor = db_connection.cursor()
    try:
        cursor.execute("DELETE FROM Employees WHERE id = %s", (id,))
        db_connection.commit()
    finally:
        cursor.close()
        db_connection.close()

# UPDATE old employee from the database
def update_employee(new_name, new_role, new_gender, new_status, id):
    db_connection = get_database_connection()
    cursor = db_connection.cursor()
    try:
        cursor.execute("UPDATE Employees SET name = %s, role = %s, gender = %s, status = %s WHERE id = %s", (new_name, new_role, new_gender, new_status, id))
        db_connection.commit()
    finally:
        cursor.close()
        db_connection.close()

# Check if an ID exists in the database
def id_exists(id):
    db_connection = get_database_connection()
    cursor = db_connection.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM Employees WHERE id = %s", (id,))
        result = cursor.fetchone()
        return result[0] > 0
    finally:
        cursor.close()
        db_connection.close()

print(fetch_employees())