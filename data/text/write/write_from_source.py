source_file_path= input("enter source file path:") or "quotes.txt"
destination_file_path= input("enter destination file path:") or "output.txt"
lines = ["I am a blessed child"]
try:
    with open (source_file_path) as source_file:
        for line in source_file:
            lines.append(line.strip())
            print("the file has been loaded")

    with open (destination_file_path) as destination_file:
        for line in lines:
            destination_file.write(f"{lines}\n")
            print("the data has been written to file")

except IOError:
    print("Cannot write data to file")