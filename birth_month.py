import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Randomdancing1!",
    database = "menagerie",
)

mycursor = mydb.cursor()

mycursor = mydb.cursor()

sql = "SELECT name, birth, MONTH(birth) AS 'MONTH(birth)' FROM pet;"


mycursor.execute(sql)

myresult = mycursor.fetchall()

mycursor.close()
mydb.close()

for x in myresult:
  print(x)