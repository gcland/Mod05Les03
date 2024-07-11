import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = "Fitness_Center_db"
    user = "root"
    password = "XXXXXXXX" #PLEASE ENTER USER PASSWORD
    host = "localhost"

    try:
        conn =  mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host=host
        )
        
        print("Connected to MySQL database successfully")
        return conn
    
    except Error as e:
        print(f"Error: {e}")
        return FileNotFoundError

