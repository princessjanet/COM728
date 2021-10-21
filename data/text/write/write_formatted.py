file_path = input("please enter file name: ") or "output.txt"
lines = "This is the first line.", "This is the second.", "This is the third line."
try:
    with open(file_path, "w") as file:
        for line in lines:
            file.write(f"{line}\n")
        print("the data has been written to the file")
except IOError:
    print("cannot write to the file")