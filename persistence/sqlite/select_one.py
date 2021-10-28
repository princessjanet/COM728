import sqlite3

# connect to the database

file_path = "users_db.db"
db = sqlite3.connect(file_path)

# query the database
cursor = db.cursor()
sql = "SELECT * FROM users;"
cursor.execute(sql)
record = cursor.fetchone()
print(record)
db.close()

