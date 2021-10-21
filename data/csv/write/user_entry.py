file_path = "user_entries.csv"
with open(file_path, "w") as file:
    file.write("Year,Artist,Song Title\n")

    print("please enter year:")
    year = int(input())

    print("please enter artist:")
    artist = input()

    print("please enter song title:")
    songtitle = input()

    file.write(f"{year}, {artist}, {songtitle}\n")