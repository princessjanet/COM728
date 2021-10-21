file_path = input ("Please enter file name: " ) or "output.txt"
try:
    with open (file_path, "w") as file:
        file.write("data has been overwritten")
        print ("data has been written to the file")

except IOError:
    print("cannot write in the file")