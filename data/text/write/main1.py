file_path = "output1.txt"

with open (file_path, "w") as file:
    file.write("id,name,category\n")

    records = ["1, Janet,Student\n", "2, Sam,Student\n"]
    for record in records:
        file.write(record)
