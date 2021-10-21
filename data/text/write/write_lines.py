file_path = input("Please enter a file name: ") or "output.txt"
lines = "This is the first line.\n", "This is the second.\n", "This is the third line.\n"
try:
    with open (file_path, "w") as file:
        file.writelines(lines)
        print("The data has been written to the file")
except IOError:
    print ("cannot write text to the file")