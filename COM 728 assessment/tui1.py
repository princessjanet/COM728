def welcome():
    print(f"\n-----------------------"
          "\nCOVID-19 (January) Data"
          "\n-----------------------")


welcome()


def error(msg):
    print("'Error!'" + msg)


error("error_msg")


def progress(operation, value):
    print(f"{operation}")

    if value == 0:
        print("has started")
    if value > 0 < 100:
        print(f"is in progress ({value}%) completed")
    if value == 100:
        print("has completed")


progress("data loading", 0)


def menu(variant=0):
    if variant == 0:
        print("Please select one of the following option:")
        print("""'[1] Process Data', '[2] Query Database', '[3] Visualise Data' and '[4] Exit'""")
        option = int(input("Your selection:"))
        return option
    if variant == 1:
        print(""" '[1] Record by Serial Number', '[2] Records by Observation Date', '[3] Group Records by Country/Region,
        '[4] Summarise Records'""")
        option = int(input("Your selection:"))
        return option
    if variant == 2:
        print(""" '[1] Setup database',
    '[2] Retrieve all countries in alphabetical order from the database',
    '[3] Retrieve confirmed cases, deaths and recoveries for an observation from the database',
    '[4] Retrieve top 5 countries for confirmed cases from the database from the database',
    '[5] Retrieve top 5 countries for deaths for specific observation dates form the database'""")
        option = int(input("Your selection:"))
        return option
    if variant == 3:
        print(""" '[1] Country/Region Pie Chart', '[2] Observations Chart', '[3] Animated Summary'""")
        option = int(input("Your selection:"))
        return option


menu(3)


def total_records(num_records):
    print(f"There are {num_records} records in the data set.")
    num_records = int(input())


total_records(100)


def serial_number():
    serial_number = int(input("please enter a serial_number for a record:"))
    return serial_number


serial_number()


def observation_dates():
    observation_dates = input("please enter some observation dates:")
    return observation_dates


observation_dates()


def display_record(record, cols=None):
    records = []
    if cols:
        for i in cols:
            records.append(record[i])
    else:
        records = record
    print(records)
display_record([1, '01/22/2020', 'Anhui', 'Mainland China', '1/22/2020 17:00', 1, 0, 0], cols= [1,3])


def display_records(records, cols=None):
    data = [[]]
    if cols:
        for i in cols:
            data.append(records[i])
    else:
        data = records
    print(data)
    A = [
        [1, '01/22/2020', 'Anhui', 'Mainland China', '1/22/2020 17:00', 1, 0, 0]
        [3, '01/22/2024', 'Eniola', 'Mainland Lagos', '10/22/2020 17:00', 5, 0, 3]
        ]
display_records(A, cols = [2.4]


if selected_option == 1:
tui.progress("data processing operation",0)
tui.menu(1)
tui.progress("data processing operation",100)
if selected_option == 1
tui.progress("record retrieval process",0)

tui.progress("record retrieval process",100)
if selected_option == 2
tui.progress("records retrieval process",0)

tui.display_records(record,cols)
tui.progress("records retrieval process",100)
if selected_option == 3
tui.progress("grouping process",0)

tui.display_records(record,cols)
tui.progress("grouping process",100)
if selected_option == 4
tui.progress("summary process",0)

tui.display_records(record,cols)
tui.progress("summary process",100)