import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Randomdancing1!",
    database = "menagerie",
)

mycursor = mydb.cursor()

mycursor = mydb.cursor()

sql = "SELECT owner, COUNT(*) FROM pet GROUP BY owner;"

mycursor.execute(sql)

myresult = mycursor.fetchall()

mycursor.close()
mydb.close()

for x in myresult:
  print(x)