import mysql.connector

from food_app.consts import DATABASE_PASSWORD

def shw_databases(user: str, password: str):
  mydb = mysql.connector.connect(
    host="localhost",
    user="Wavy",
    password= DATABASE_PASSWORD
  )
  mycursor = mydb.cursor()

  mycursor.execute("SHOW DATABASES")

  for x in mycursor:
    print(x)

