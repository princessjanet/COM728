import sqlite3

print("Please enter the user id:")
id = int(input())

file_path = "users_db.db"
db = sqlite3.connect(file_path)
cursor = db.cursor()
sql = "SELECT* FROM users where id=?"
values = [id]

cursor.execute(sql, values)
record = cursor.fetchone()
print(record)
db.close()
print("Current user details are as follows:")
print(f"id:{record[0]}, height: {record[1]}, weight: {record[2]}, date_of_birth:{record[3]}")
print("What would you like to change?:")
height = input()
print("What is the new value for height?:")
sql = "UPDATE user SET height"
cursor.execute(sql)
db.commit()


