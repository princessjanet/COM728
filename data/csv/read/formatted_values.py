import csv

file_path= "../songs.csv"
with open (file_path) as file:
    csv_reader = csv.reader(file)
    headings= next(csv_reader)

    for record in csv_reader:
        print(f"[{record[3]}],{record[0]},(by {record[1]})\n")