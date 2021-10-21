file_path = input("enter the file name: ")
try:
    with open(file_path) as file:
        lines = file.readlines()
        print(lines)

except IOError:
    print("Cannot read file")