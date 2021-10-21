file_path = input("Enter file name: ") or "quotes.txt"
try:
    with open(file_path)as file:
        for line in file.readlines():
            print(line.strip())
except IOError:
    print("cannot read file")