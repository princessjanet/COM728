import sqlite3
file_path = "users_db.db"
db = sqlite3.connect(file_path)
cursor = db.cursor()
sql = "SELECT* FROM users;"
cursor.execute(sql)
print("Enter the number of record to be read:")
number_of_record = input()
if number_of_record == "":
    records = cursor.fetchaall()
else:
    records = cursor.fetchmany(int(number_of_record))
db.close()
print(records)
