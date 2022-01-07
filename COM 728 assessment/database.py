"""
This module is responsible for setting up and querying the database.
"""

"""
Task 22 - 26: Write suitable functions to query the database as follows:

Setup database
Retrieve the names of all (unique) countries in alphabetical order
Retrieve the number of confirmed cases, deaths and recoveries for a specified observation / serial number.
Retrieve information for the top 5 countries for confirmed cases
Retrieve information for the top 5 countries for death for specific observation dates


The should do the following:
- Take a list of records as a parameter
- Use the list passed as a parameter value to create and populate a suitable database. You are required to design a
suitable (small) database.
- It is recommended that you complete this function last and start by creating your database using a tool such as
SQL DB Browser. This would allow you to complete the other database functions first.  You can then complete this
function to generate the database via code.

Each function for querying the database should follow the pattern below:
- Take no parameters
- Query the database appropriately. You may use the module 'tui' to retrieve any additional information 
required from the user to complete the querying.
- Return a list of records as retrieved from the database

"""

# TODO: Your code here
from dns.resolver import query
import sqlite3
import tui
import process
def create_table():
    cursor = db.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table = [x[0] for x in cursor.fetchall() if v[0] != "sqlite_sequence"]
    cursor.close()
    return table
def database_setup(records):
    db = sqlite3.connect('covid.db')
    print(dir(db))
    val = [tuple (y) for y in records]
    try:
        sql = "INSERT INTO covid_19_data (Sno,ObservationDate,Province,Country,LastUpdate,Confirmed,Deaths,Recovered) VALUES (?,?,?,?,?,?,?,?);"
        db.executemany(sql,val)
        db.commit()
    except IOError:
        tui.error('cannot create table')

def retrieve_country_name_alphabetically():
    countries = []
    db = sqlite3.connect('covid19.db')
    try:
        query = "SELECT Distinct Country FROM covid_19_data"
        cursor = db.execute(query)
        result = cursor.fetchall()
        country = [x[0] for x in result]
    except IOError:
        tui.error('error retrieving country name')
    db.close()
    return sorted(countries)

def retrieve_confrimedcases():
    result =[]
    db = sqlite3.connect('covid.db')
    print('[1] By Observation Date\n[2] By Serial Number')
    selected_option = input('Select 1 or 2: :' )
    while selected_option not in ('1','2'):
        selected_option = input('Select 1 or 2: :' )
    if selected_option == '1':
        date = tui.observation_dates()
        date = str(tuple(date))[0:-2]+')' if str(tuple(date)).endswith(',)') else str(tuple(date))
        query = 'SELECT * FROM covidstatus WHERE ObservationDate IN %s' % date
    else:
        serial = tui.serial_number()
        query = 'SELECT * FROM covidstatus WHERE Sno = %s' %str(ser)
    try:
        cursor = db.execute(query)
        result =cursor.fetchall()
    except IOError:
        tui.error('cannot query data')
    db.close()
    return result

def retrieve_top_confirmed():
    result = []
    db = sqlite3.connect('covid.db')
    query = 'SELECT  Sno,ObservationDate,Province,Country,LastUpdate,sum(Confirmed),Deaths,Recovered FROM covidstatus GROUP BY(Country) ORDER BY sum(Confirmed) DESC'
    try:
    cursor = db.execute(query)
    result = cursor.fetchmany(size=5)
    except IOError:
        tui.error('cannot query data')
    db.close()
    return result

def retrieve_


if __name__ == '__main__':
    setup([[2, 'dd', 'dd', 'dd', 'dd', 2, 2, 2]])