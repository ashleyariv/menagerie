import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Randomdancing1!",
    database = "menagerie",
)

mycursor = mydb.cursor()

sql = """
INSERT INTO pet (name, owner, species, sex, birth, death) 
VALUES (%s, %s, %s, %s, %s, %s)
"""


values = [
    ('Fluffy', 'Harold', 'cat', 'f', '1993-02-04', None),
    ('Claws', 'Gwen', 'cat', 'm', '1994-03-17', None),
    ('Buffy', 'Harold', 'dog', 'f', '1989-05-13', None),
    ('Fang', 'Benny', 'dog', 'm', '1990-08-27', None),
    ('Bowser', 'Diane', 'dog', 'm', '1979-08-31', '1995-07-29'),
    ('Chirpy', 'Gwen', 'bird', 'f', '1998-09-11', None),
    ('Whistler', 'Gwen', 'bird', 'm', '1997-12-09', None),
    ('Slim', 'Benny', 'snake', 'm', '1996-04-29', None)
]

mycursor.executemany(sql, values)
mydb.commit()
mycursor.close()
mydb.close()

print(mycursor.rowcount, "was inserted.")