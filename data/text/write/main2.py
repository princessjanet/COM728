file_path = "output2.txt"

with open (file_path, "w") as file:
    file.write("id,name,category\n")

    for count in range(2):
        print("please enter your id")
        id = int(input()

        print("Please enter your name")
        name =input()

        print("please enter your category")
        category =input()

        file.write(f"{id},{name},{category}\n")

