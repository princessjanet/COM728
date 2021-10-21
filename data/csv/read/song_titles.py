import csv
file_path = "../songs.csv"
with open (file_path) as file:
    csv_reader = csv.reader(file)
    Headings = next(csv_reader)

    for record in csv_reader:
        print(record[0])

