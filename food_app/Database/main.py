import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="your_database"
)

cursor = conn.cursor()