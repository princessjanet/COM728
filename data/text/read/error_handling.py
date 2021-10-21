bad_file_path = "bad_file"
try:
    with open(bad_file_path) as file:
        lines= file.readlines()
        print(lines)
except IOError:
         print("cannot read file")
