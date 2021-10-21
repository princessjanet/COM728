import csv
file_path = "../songs.csv"

with open (file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(headings)