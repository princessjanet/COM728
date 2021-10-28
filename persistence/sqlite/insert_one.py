import sqlite3
print("Please enter the name of the user:")
name =input()
print("Please enter the height of the user:")
height = float(input())
print("Please enter the weight of the user:")
weight = float(input())
print("Please enter the user's date of birth:")
date_of_birth =input()

file_path = "users_db.db"
db = sqlite3.connect(file_path)
cursor = db.cursor()
sql = " INSERT INTO users (name, height, weight, date_of_birth)  values(?,?,?,?)"
values = [name, height, weight, date_of_birth]
cursor.execute(sql,values)
rowid = cursor.lastrowid
db.commit()
print(cursor.lastrowid)
