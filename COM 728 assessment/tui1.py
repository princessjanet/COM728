def welcome():
    print(f"\n-----------------------"
          "\nCOVID-19 (January) Data"
          "\n-----------------------")


welcome()


def error(msg):
    print("'Error!'" + msg)


error("error_msg")


def progress(operation, value):
    print(f"{operation} status")

    if value == 0:
        print("has started")
    if value > 0 < 100:
        print(f"is in progress ({value}%) completed")
    if value == 100:
        print("has completed")


progress("calculation", 50)


def menu(variant=0):
    if variant == 0:
        print("""'[1] Process Data', '[2] Query Database', '[3] Visualise Data' and '[4] Exit'""")
        return int(variant)
    if variant == 1:
        print(""" '[1] Record by Serial Number', '[2] Records by Observation Date', '[3] Group Records by Country/Region,
        '[4] Summarise Records'""")
        return int(variant)
    if variant == 2:
        print(""" '[1] Setup database',
    '[2] Retrieve all countries in alphabetical order from the database',
    '[3] Retrieve confirmed cases, deaths and recoveries for an observation from the database',
    '[4] Retrieve top 5 countries for confirmed cases from the database from the database',
    '[5] Retrieve top 5 countries for deaths for specific observation dates form the database'""")
        return int(variant)
    if variant == 3:
        print(""" '[1] Country/Region Pie Chart', '[2] Observations Chart', '[3] Animated Summary'""")
        return int(variant)


menu(3)


def total_records(num_records):
    print(f"There are {num_records} records in the data set.")
    num_records = int(input())


total_records(100)
