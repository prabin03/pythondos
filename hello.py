import sqlite3
import csv

def create_connection():
    try:
        con = sqlite3.connect("hellos.sqlite")
        return con
    except Exception as e:
        print(f"Error {e}")

INPUT_STRING = """
    Enter the option:
        1. Create the TABLE
        2. DUMP users from csv INTO users TABLE
        3. ADD new user into users TABLE
        4. QUERY all users from TABLE
        5. QUERY user by id from TABLE
        6. QUERY specified no. of records from TABLE
        7. DELETE all users
        8. DELETE user by id
        9. UPDATE user
        10.Press any key to EXIT 
    """


def create_tables(conn):
    CREATE_HELLOS_TABLES_QUERY = """
        CREATE TABLE IF NOT EXISTS hellos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name CHAR(255) NOT NULL,
            last_name CHAR(255) NOT NULL,                   
            company_name CHAR(255) NOT NULL,
            address CHAR(255) NOT NULL,           
            city CHAR(255) NOT NULL,
            county CHAR(255) NOT NULL,
            state CHAR(255) NOT NULL,
            zip REAL NOT NULL,
            phone1 CHAR(255) NOT NULL,
            phone2 CHAR(255) NOT NULL,
            email CHAR(255) NOT NULL,
            web text
        );

    """
    cur = conn.cursor()
    cur.execute(CREATE_HELLOS_TABLES_QUERY)
    print("hellos table was created successfully.")

def read_csv():
    hellos = []
    with open("sample_users.csv","r") as f:
        ook = csv.reader(f)
        for user in ook:
            hellos.append(tuple(user))
    
    return hellos[1:]

def insert_users(con, hellos):
    user_add_query = """
        INSERT INTO hellos 
        (
            first_name, 
            last_name, 
            company_name, 
            address, 
            city, 
            county, 
            state, 
            zip, 
            phone1, 
            phone2, 
            email, 
            web
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    cur = con.cursor()
    cur.executemany(user_add_query, hellos)
    con.commit()
    print(f"{len(hellos)} users were imported sucessfully")

def main():
    con = create_connection()
    user_input = input(INPUT_STRING)
    if user_input == "1":
        create_tables(con)
    elif user_input == "2":
        hellos = read_csv()
        insert_users(con, hellos) 

    elif user_input == "3":
        data = []
        for column in COLUMNS:
            column_value = input(f"Enter the value of {column}:")
            data.append(column_value)
        insert_users(con, [tuple(data)])

    if user_input == "4":
        create_tables(con)


main()