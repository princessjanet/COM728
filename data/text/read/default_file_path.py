file_path = input("Enter the file name: ") or "quotes.txt"
try:
    with open(file_path) as file:
        lines = file.readlines()
        print(lines)
except IOError:
    Print("cannot read file")