import csv

with open("data.csv") as file:
    csv_reader = csv.reader(file)
    headings = next(csv_reader)

    for record in csv_reader:
         print(f"name is {record[1]}")