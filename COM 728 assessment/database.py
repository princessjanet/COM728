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






    if __name__ == '__main__':
        setup([[2, 'dd', 'dd', 'dd', 'dd', 2, 2, 2]])