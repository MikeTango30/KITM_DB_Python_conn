import sqlite3
import pprint
# from employee import employee


def create_employee_table():
    connection = sqlite3.connect("employee.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
                                            id integer PRIMARY KEY,
                                            first_name text,
                                            last_name text,
                                            pay_roll integer)""")
    connection.commit()
    connection.close()


def create_employee():
    try:
        connection = sqlite3.connect("employee.db")
        connection_cursor = connection.cursor()

        connection_cursor.execute("""INSERT INTO employees (first_name, last_name, pay_roll) 
                                                        VALUES ('John','Smith',70000)""")
        connection.commit()
        connection.close()
    except:
        print(sqlite3.Error)
    finally:
        connection.close()


def select_employee():
    try:
        connection = sqlite3.connect("employee.db")
        connection_cursor = connection.cursor()

        connection_cursor.execute("""SELECT * FROM employees""")

        connection.commit()

        rows = []
        for row in connection_cursor.execute('SELECT * FROM employees'):
            rows.append(row)
        print(rows)

        pp = pprint.PrettyPrinter()
        pp.pprint(rows)
        connection.close()
    except:
        print(sqlite3.Error)
    finally:
        connection.close()


def update_employee():
    try:
        connection = sqlite3.connect("employee.db")
        connection_cursor = connection.cursor()

        connection_cursor.execute("""UPDATE employees SET first_name='Jack' WHERE first_name='John'""")

        connection.commit()
        connection.close()
    except:
        print(sqlite3.Error)
    finally:
        connection.close()


def delete_employee():
    try:
        connection = sqlite3.connect("employee.db")
        connection_cursor = connection.cursor()

        connection_cursor.execute("""DELETE FROM employees WHERE first_name='Jack'""")

        connection.commit()
        connection.close()
    except:
        print(sqlite3.Error)
    finally:
        connection.close()


create_employee_table()
create_employee()
update_employee()
delete_employee()
select_employee()
