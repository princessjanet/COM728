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

def retrieve_total_number_of_records(loaded):
   return len (loaded)

def retrieve_records_by_serial_number(records,serial):
    """
        :records: A list of records
        :serial: An interger refference to a record
        :return: list of a certain record for the serial number
        """

    for record in records:
        if record[0] == serial:
            return record
    return []

def retrieve_records_by_observation_date(records,dates):
    """
        :records: A list of records
        :dates: A list of observation dates
        :return: list of a certain record for the serial number if it exist else None
        """
    exist = []
    for date in dates:
        for record in records:
            if date in record[1]:
                exist.append(record)
    return exist


def retrieve_record_groupby_country(records):
    region = input("what is your country/region?")
    temp = {"country": region, "confirmed cases":0,"death": 0, "recovered":0}
    for record in records:
        confirmed = records[5]
        death = record[6]
        recovered = record[7]
        if record[3] ==region:
            temp["confirmed cases"]+=confirmed
            temp["deaths"]+=death
            temp['recovered']+=Recovered
    return[temp]



