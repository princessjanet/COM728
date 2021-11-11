import database


def menu():
    print("""Please select one of the following options:
[1] Display presenters
[2] Display events
[3] Display presenters for event
[4] Display events for presenter""")
    option = int(input("your selection"))
    return option


def run():
    option = menu()
    if option == 1:
        database.display_presenters()
    elif option == 2:
        database.display_events()
    elif option == 3:
        database.display_presenters_specified_event()
    elif option == 4:
        database.display_events_specified_presenter()


if __name__ == "__main__":
    run()
