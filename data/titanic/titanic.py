import csv

file_path = "titanic.csv"
records = []
print("loading data....", end="")
try:
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)

        for line in csv_reader:
            records.append(line)

    print("Done")
    print(f"successfully loaded{len(records)} record.")
    print(
        " Please select one of the following options: \n [1] Display the names of all passengers\n [2] Display the number of passengers that survived\n [3] Display the number of passengers per gender\n [4] Display the number of passengers per age group")
    selected_option = int(input())
    print(f"you have selected option: {selected_option}")
    if selected_option == 1:
        print("The names of the passengers are...")
        for record in records:
            passenger_name = record[3]
            print(f" {passenger_name}")
    if selected_option == 2:
        num_survived = 0
        for record in records:
            survival_status = int(record[1])
            if survival_status == 1:
                num_survived += 1
        print(f"{num_survived}passengers survived")

    if selected_option == 3:
        females = 0
        males = 0
        for record in records:
            gender = (record[4])
            if gender.lower() == "male":
                males += 1
            else:
                females += 1
        print(f"females:{females}, males:{males}")

    if selected_option == 4:
        children = 0
        adults = 0
        elders = 0
        for record in records:
            age = record[5]

            if age and age != "":
                age = float(age)

                if age < 18:
                    children += 1
                if age > 65:
                    elders += 1
                else:
                    adults += 1
        print(f" children:{children}, adults:{adults}, elders:{elders}")

except IOError:
    print("cannot load file")
