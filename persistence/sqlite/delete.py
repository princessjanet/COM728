import sqlite3

print("Please enter a user id:")
id = int(input())

file_path = "users_db.db"
db = sqlite3.connect(file_path)
cursor = db.cursor()

sql = "DELETE FROM users WHERE id=?"
values = [id]

cursor.execute(sql, values)
db.commit()
db.close()

