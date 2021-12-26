"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""

# TODO: Your code here

import tui

def retrieve_total_number_of_records():
    records = []
    num_records = len(records)
retrieve_total_number_of_records()

def retrieve_records_by_serial_number():
    records = []
    tui.serial_number()
    print(records{tui.serial_number})
retrieve_records_by_serial_number()

def retrieve_records_by_observation_date():
    records = []
    tui.observation_dates()
    observation_dates = input("Please enter observation dates")
    print(records[observation_dates])



