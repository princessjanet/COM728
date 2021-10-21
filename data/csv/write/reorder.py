import csv

file_path ="../songs.csv"
des_file_path = "output.csv"
with open(file_path,"r")as file:
    with open(des_file_path, "w") as des_file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        des_file.write(str(headings))

        for record in csv_reader:
            print(f"\n {record[3]},{record[2]}, {record[1]}, {record[0]}")





