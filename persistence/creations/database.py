import sqlite3


def display_presenters():
    file_path = "event.db"
    db = sqlite3.connect(file_path)
    cursor = db.cursor()
    sql = "SELECT presenter.name, organisation.name FROM presenter INNER JOIN organisation ON " \
          "presenter.organisation_id=organisation.id "
    cursor.execute(sql)
    records = cursor.fetchall()
    print("The following are the name of all the presenters and their organisation")
    for record in records:
        print(f"presenter:{record[0]}, organisation:{record[1]}")
    db.close()


def display_events():
    file_path = "event.db"
    db = sqlite3.connect(file_path)
    cursor = db.cursor()
    sql = "SELECT events.name, location.city, location.country from events INNER JOIN location ON events.location_id=location.id"
    cursor.execute(sql)
    records = cursor.fetchall()
    print("The following events will be taken place in this location:")
    for record in records:
        print(f"event:{record[0]}, city:{record[1]}, country:{record[2]}")
    db.close()


def display_presenters_specified_event():
    file_path = "event.db"
    db = sqlite3.connect(file_path)
    cursor = db.cursor()
    event_id = int(input("please enter event id"))
    sql = "SELECT events.name FROM events WHERE events.id=?;"
    values = [event_id]
    cursor.execute(sql, values)
    records = cursor.fetchone()

    sql = "SELECT presenter.name, events.name, events.host_organisation FROM presenter INNER JOIN events_presenter ON " \
          "events_presenter.presenter_id= presenter.id INNER JOIN events ON events_presenter.events_id = events.id " \
          "WHERE events.id=? "
    cursor.execute(sql, values)
    records = cursor.fetchall()
    print("The presenters for this event are listed below:")
    for record in records:
        print(f"presenter: {record[0]}, event: {record[1]}")
    db.close()


def display_events_specified_presenter():
    file_path = "event.db"
    db = sqlite3.connect(file_path)
    cursor = db.cursor()
    presenter_id = int(input("Please enter presenter id:"))
    sql = "SELECT presenter.name FROM presenter WHERE presenter.id=?"
    values = [presenter_id]
    cursor.execute(sql, values)
    records = cursor.fetchone()

    sql = "SELECT events.name, presenter.name FROM events INNER JOIN events_presenter ON events_presenter.events_id = " \
          "events.id INNER JOIN presenter ON events_presenter.presenter_id= presenter.id WHERE presenter.id=? "
    cursor.execute(sql,values)
    print("The events for this presenter is listed below:")
    for record in records:
        print(f"{record[0]}")
