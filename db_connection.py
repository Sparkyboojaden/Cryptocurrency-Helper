import mysql.connector

#mydb is the object that stores all of the connection fields to the db 
mydb= mysql.connector.connect(
  host = "hot",
  database = "db",
  user = "user",
  password = "pw"
)


