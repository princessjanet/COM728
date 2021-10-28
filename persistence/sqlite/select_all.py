import sqlite3

file_path = "users_db.db"
db = sqlite3.connect(file_path)
cursor = db.cursor()
sql = "SELECT * FROM users;"
cursor.execute(sql)
records = cursor.fetchall()
for record in records:
    print(record)
db.close()



