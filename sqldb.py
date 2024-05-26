import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "giorgowkatsaros",
    passwd = "12345"
        ) 
print(mydb)
