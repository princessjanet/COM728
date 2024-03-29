"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, querying of the database and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any database related querying should be done using the appropriate functions the module 'database'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""


# Task 10: Import required modules2
# TODO: Your code here
import tui
import csv
import process
import database
import visual

# Task 11: Create an empty list named 'covid_records'.
# This will be used to store the data read from the source data file.
# TODO: Your code here
covid_records = []


def run():
    tui.welcome()
    file = 'covid_19_data.csv'
    tui.progress('Loading Data', 0)
    try:
        with open(file, 'r') as f:
            data = f.readlines()[1:]

            covid_records = [[int(x) if x.isnumeric() else x for x in line.strip().split(',')] for line in data]

    except Exception as e:
        tui.error(str(e))
    tui.progress('Loading Data', 100)
    tui.total_records(process.retrieve_total_number_of_records(covid_records))

    while True:
        # Task 14: Using the appropriate function in the module 'tui', display a menu of options
        # for the different operations that can be performed on the data (menu variant 0).
        # Assign the selected option to a suitable local variable
        # TODO: Your code here
        selected_option = tui.menu(variant=0)

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an individual record by serial number then
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the record and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve (multiple) records by observation dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve records with
        #       - Use the appropriate function in the module 'tui' to display the retrieved records.
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group records by country/region then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the records
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the records then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the records.
        #       - Use the appropriate function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
        # TODO: Your code here
        if selected_option == 1:
            selected_option1 = tui.menu(variant=1)
            if selected_option1 == 1:
                tui.progress("record retrieval process",0)
                serial = tui.serial_number()
                record = process.retrieve_records_by_serial_number(covid_records,serial)
                tui.display_record(record)
                tui.progress("record retrieval process",100)
            elif selected_option1 == 2:
                tui.progress("record retrieval process", 0)
                date = tui.observation_dates()
                record = process.retrieve_records_by_observation_date(covid_records, date)
                tui.display_record(record)
                tui.progress("record retrieval process", 100)
            elif selected_option1 == 3:
                tui.progress("grouping process", 0)
                record = process.retrieve_record_groupby_country(covid_records)
                tui.display_record(record)
                tui.progress("grouping process", 100)
            elif selected_option1 == 4:
                tui.progress("summary process", 0)
                record = process.retrieve_summary(covid_records)
                tui.display_record(record)
                tui.progress("summary process", 100)



        # Task 21: Check if the user selected the option for setting up or querying the database.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # database querying operation has started.
        # - Query the database by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what querying is to be done.
        #   - call the appropriate function in the module 'database' to retrieve the results
        #   - call the appropriate function in the module 'tui' to display the results
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # database querying operation has completed.
        # TODO: Your code here
        elif selected_option == 2:
            selected_option1 = tui.menu(variant=2)
            if selected_option1 == 1:
                tui.progress('database querying operation',0)
                database.database_setup(covid_records)
                tui.progress('database querying operation',100)
            elif selected_option1 == 2:
                tui.progress('database querying operation',0)
                country = database.retrieve_country_name_alphabetically()
                tui.display_records(country)
                tui.progress('database querying operation',100)
            elif selected_option1 == 3:
                tui.progress('database querying operation',0)
                cases = database.retrieve_confirmedcases()
                tui.display_records(cases)
                tui.progress('database querying operation',100)
            elif selected_option1 == 4:
                tui.progress('database querying operation', 0)
                top_confirmed = database.retrieve_top_confirmed()
                tui.display_records(top_confirmed)
                tui.progress('database querying operation', 100)
            elif selected_option1 == 5:
                tui.progress('database querying operation', 0)
                top_death = database.retrieve_top_death()
                tui.display_records(top_death)
                tui.progress('database querying operation', 100)



        # Task 27: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual'
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        # TODO: Your code here
        elif selected_option == 3:
            selected_option1 = tui.menu(variant=3)
            if selected_option1 == 1:
                tui.progress('data visualisation operation',0)
                visual.pie_chart()
                tui.progress('data visualisation operation',100)
            elif selected_option1 == 2:
                tui.progress('data visualisation operation', 0)
                visual.bar_chart()
                tui.progress('data visualisati2on operation', 100)
            elif selected_option1 == 3:
                tui.progress('data visualisation operation',0)
                visual.animate()
                tui.progress('data visualisation operation',100)
        # Task 31: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TODO: Your code here
        elif selected_option == 14:
            break
        # Task 32: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TODO: Your code here
        else:
            tui.error('Select between option 1 to 4')



if __name__ == "__main__":
    run()
