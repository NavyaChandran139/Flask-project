import mysql.connector

DB =mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = 'exam'
)

CR = DB.cursor(dictionary=True)