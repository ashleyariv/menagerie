import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Randomdancing1!",
    database = "menagerie",
)

mycursor = mydb.cursor()

mycursor = mydb.cursor()

sql = "SELECT name, birth FROM pet;"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)