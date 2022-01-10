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
import csv


def database_setup(records = None):
    db = sqlite3.connect('covid.db')
    cursor = db.cursor()
    tbl_sql = '''CREATE TABLE IF NOT EXISTS "country" (
	"SNo"	INTEGER,
	"Country"	TEXT,
	"Province"	TEXT,
	PRIMARY KEY("SNo")
);'''
    sql = """
        BEGIN TRANSACTION;
        CREATE TABLE IF NOT EXISTS "cases" ("SNo" INTEGER,
                           "Confirmed" INTEGER,
                           "Deaths" INTEGER,
                           "Recovered" INTEGER,
                           "ObservationDate" TEXT,
                           "countrysno" INTEGER,
                           PRIMARY KEY("SNo" )
                          );
                        """
    cursor.executescript(sql)
    cursor.executescript(tbl_sql)


    file = open("covid_19_data.csv")
    records = csv.reader(file)
    headings = next(records)
    # populate country data
    for record in records:
        query = "INSERT INTO country (SNo, Country,Province) VALUES (?,?,?)"
        value = [record[0],record[3], record[2]]
        try:
            cursor.execute(query, value)
        except Exception as e:
            tui.error(f'Inserting data to table country {e}')
    # populate cases
    file = open("covid_19_data.csv")
    records = csv.reader(file)
    for record in records:
        query = "INSERT INTO cases (SNo, Confirmed,Deaths,Recovered,ObservationDate,countrysno) VALUES(?,?, ?, ?,?,?);"
        value = [record[0],record[5], record[6], record[7],record[1],record[0]]
        try:
            cursor.execute(query, value)
            db.commit()

        except Exception as e:
            tui.error(f'Inserting case data to table cases {e}')
    db.close()
    file.close()



def retrieve_country_name_alphabetically():
    country = []
    db = sqlite3.connect('covid.db')
    try:
        cursor = db.cursor()
        query = "SELECT Distinct Country FROM country"
        cursor.execute(query)
        result = cursor.fetchall()
        country = [x[0] for x in result]
    except IOError:
        tui.error('error retrieving country name')
    db.close()
    return sorted (country)

def retrieve_confirmedcases():
    result =[]
    db = sqlite3.connect('covid.db')
    print('[1] By Observation Date\n[2] By Serial Number')
    selected_option = input('Select 1 or 2: :' )
    while selected_option not in ('1','2'):
        selected_option = input('Select 1 or 2: :' )
    if selected_option == '1':
        date = tui.observation_dates()
        date = str(tuple(date))[0:-2]+')' if str(tuple(date)).endswith(',)') else str(tuple(date))
        query = 'SELECT * FROM cases WHERE ObservationDate IN %s' % date
    else:
        serial = tui.serial_number()
        query = 'SELECT * FROM cases WHERE Sno = %s' %str(serial)
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
    query = 'SELECT  cases.Sno,cases.ObservationDate,sum(cases.Confirmed),cases.Deaths,' \
            'cases.Recovered, country.Country FROM cases,country WHERE country.SNo == cases.countrysno GROUP BY(country.Country) ORDER BY sum(cases.Confirmed) DESC'
    try:
        cursor = db.execute(query)
        result = cursor.fetchmany(size=5)
    except IOError:
        tui.error('cannot top confirmed cases data')
    db.close()
    return result

def retrieve_top_death():
    result = []
    db = sqlite3.connect('covid.db')
    date = tui.observation_dates()
    date = str(tuple(date))[0:-2]+')' if str(tuple(date)).endswith(',)') else str(tuple(date))
    print(date)
    query = '''SELECT  cases.Sno,cases.ObservationDate,cases.Confirmed,sum(cases.Deaths),
            cases.Recovered, country.Country FROM cases, 
            country WHERE cases.countrysno = country.SNo AND cases.ObservationDate in %s  GROUP BY(country.Country) ORDER BY sum(cases.Deaths) DESC;''' %date
    try:
        cursor = db.execute(query)
        result = cursor.fetchmany(size=5)
    except Exception as e:
        tui.error(f'cannot retrieve top death data {e}')
    db.close()
    return result

def retrieve_summaryby():
    db = sqlite3.connect('covid.db')
    query = "SELECT cases.ObservationDate,sum(cases.Confirmed), sum(cases.Deaths), " \
            "sum(cases.Recovered),country.Country FROM cases,country where cases.countrysno==country.SNo and country.Country = '%s' GROUP BY ObservationDate" %country
    result = []
    try:
        cursor = db.execute(query)
        result = cursor.fetchall()
    except IOError:
        tui.error('cannot retrieve summary of data')
    db.close()
    return result



if __name__ == '__main__':
    r = retrieve_top_confirmed()
    for data in r:
        print(data)