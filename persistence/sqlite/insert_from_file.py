import sqlite3
import csv
print("please enter the file path:")
file_path = input()
data = []

with open(file_path) as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        data.append(line)

print("Inserting data into the database...")
db = sqlite3.connect("users_db.db")
cursor = db.cursor()
for item in data:
    sql = "INSERT INTO users (name, height, weight, date_of_birth) VALUES (?, ?, ?, ?)"
    values = (item[0], item[1], item [2], item [3])
    cursor.execute(sql, values)
db.commit()
