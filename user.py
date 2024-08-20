import sqlite3
import csv

#git init
# git add
# git commit -m "message "
# copy paste from github repositry created above
#  git remote add origin https://github.com/prabin03/Python-project.git
# git push -u origin main

# after changing file
# git status # check what happens in the file
# git diff
# git add .
# git commit -m "message "
# git push origin

def create_connection():
    try:
        conn = sqlite3.connect("users.sqlite")
        return conn
    except Exception as e:
        print(f"Error:,{e}")

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
    CREATE_USER_TABLES_QUERY = """
        CREATE TABLE IF NOT EXISTS users(
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
    cur.execute(CREATE_USER_TABLES_QUERY)
    print("user table was created successfully.")

 

def read_csv():
    users = []
    with open ("sample_users.csv","r") as f:
        data = csv.reader(f)
        for user in data:
            users.append(tuple(user))
    
    return users[1:]


def insert_users(conn, users):
    user_add_query = """
        INSERT INTO users 
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
    cur = conn.cursor()
    cur.executemany(user_add_query, users)
    conn.commit()
    print(f"{len(users)} users were imported sucessfully")


#4
def select_user(conn):
    cur=conn.cursor()
    users=cur.execute("SELECT * FROM users")
    for user in users:
     print(user)
#5
def select_user_by_id(conn,user_id):
    cur=conn.cursor()
    users=cur.execute("SELECT * FROM users WHERE id=?;",(user_id,))
    for user in users:
        print(user)
#6
def select_specified_records(conn,no_of_users=0):
    cur=conn.cursor()
    if no_of_users:
        users=cur.execute("SELECT * FROM users LIMIT ? ",(no_of_users,))
    # else:
    #     users=cur.execute("SELECT * FROM users")
    for user in users:
        print(user)
# 7
def delete_users(conn):
    cur = conn.cursor()
    cur.execute("DELETE from users;")
    conn.commit()
    print("All the users were deleted sucessfully")
# 8
def delete_users_by_id(conn, user_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM users where id = ?",(user_id,))
    conn.commit()
    print(f"[{id}] has been deleted")
COLUMNS = (
   "first_name", 
   "last_name",     
   "company_name", 
   "city", 
   "county", 
   "state", 
   "zip", 
   "phone1", 
   "phone2", 
   "email", 
   "web"
)

def update_users_by_id(conn,user_id, column_name, column_value):
    update_query = f"UPDATE users set {column_name}=? where id =?;"
    cur = conn.cursor()
    cur.execute(update_query,(column_value, user_id))
    conn.commit()
    print(f"[{column_name}] was update with value[{column_value}] of user with id [{user_id}]")



def main():
    conn = create_connection()
    user_input = input(INPUT_STRING)
    if user_input == "1":
        create_tables(conn)
    elif user_input == "2":
        users = read_csv()
        insert_users(conn, users)
   
    elif user_input == "3":
        data = []
        for column in COLUMNS:
            column_value = input(f"Enter the value of {column}:")
            data.append(column_value)
        insert_users(conn, [tuple(data)])

    elif user_input == "4":
        select_user(conn)    
    elif user_input == "5":
        user_id = input("Enter user id: ")
        if user_id.isnumeric():
            select_user_by_id(conn, user_id)
    elif user_input == "6":
        no_of_users = input("Enter the no of users to fetch: ")
        if no_of_users.isnumeric() and int(no_of_users) > 0:
            select_specified_records(conn, no_of_users)
    elif user_input == "7":
        confirm = input("Are you sure you want to delete all users? (y/n):")
        if confirm == "y":
            delete_users(conn)

    elif user_input == "8":
        user_id = input("Enter user id: ")
        if user_id.isnumeric():
            delete_users_by_id(conn,user_id)

    elif user_input == "9":
        user_id = input("Enter user id: ")
        if user_id.isnumeric():
            column_name = input(f"Enter the column you want to edit. Please make sure column is with in [{COLUMNS}]")
            if column_name in COLUMNS:
                column_value = input(f"Enter the value of {column_name}:")
                update_users_by_id(conn, user_id, column_name, column_value)
        





main()









# def add_user(conn):
#     first_name = input("Enter first name: ")
#     last_name = input("Enter name: ")
#     company_name = input("Enter company name; ")
#     address = input("Enter address: ")
#     city = input("Enter city: ")
#     county = input("Enter county: ")
#     state = input("Enter state: ")
#     zip = input("Enter zip: ")
#     phone1 = input("Enter phone1: ")
#     phone2 = input("Enter phone2: ")
#     email = input("Enter email: ")
    
#     INSERT_USER_TABLES_QUERY = ("INSERT INTO users (first_name, last_name, company_name, address, city, county, state, zip, phone1, phone2, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (first_name, last_name, company_name, address, city, county, state, zip, phone1, phone2, email))

# def user_add(conn):
#     cur = con.cursor()
#     cur.execute(INSERT_USER_TABLES_QUERY)
#     print("User added successfully.")

