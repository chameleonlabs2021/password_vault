import sqlite3
import string
import random



database = r"C:\big data\python_projects\SQLliteDB\pythonsqlite.db"
def table_cre():
    try:
        sqliteConnection = sqlite3.connect(database)
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS password (
                                        website text NOT NULL,
                                        password text NOT NULL
                                                );"""                      
        sqlite_insert_query = """INSERT INTO password (website,password) 
        VALUES ('rahulpoolanchalil@gmail.com','98509745');"""
        sqlite_select_query = """INSERT INTO password (website,password) 
        VALUES ('rahulpoolanchalil@gmail.com','98509745');"""

        count = cursor.execute(sqlite_insert_query)
        print(cursor.execute(sqlite_select_query))
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.execute("SELECT * FROM password")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            #  cursor.execute("SELECT * FROM password WHERE priority=?", (priority,))

def select_func(website):
    try:
        sqliteConnection = sqlite3.connect(database)
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        # cursor.execute("""delete from password""")
        # sqliteConnection.commit()        
        cursor.execute("SELECT * FROM password where website= ?", (website,))
        rows = cursor.fetchall()
        print(rows)
        
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
   
def insert_func(website,newpassword):
    # print("Entered Insert function")
    
    website=str(website)
    newpassword=str(newpassword)
    # print("newpass:",newpassword)
    # print("website:",website,"password:",newpassword)
    try:
        sqliteConnection = sqlite3.connect(database)
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        # cursor.execute("""delete from password""")
        # sqliteConnection.commit()        
        cursor.execute("SELECT * FROM password where website= ?", (website,))
        rows = cursor.fetchall()
        print(type(rows))
        print(rows)
        if len(rows) ==0 :
            print("Going to insert the data",website,newpassword)
            cursor.execute("""INSERT INTO password (website,password) VALUES (?,?)""",(website,newpassword))
            sqliteConnection.commit()
        else:
            user_input=int(input("""Entry already exists in the vault
            1.Update the password
            2. quit \n"""))
            if user_input == 1:
                for row in rows:
                    print(row)
                    print(row[0])
                    cursor.execute("""update password set password=?  where website=?""",(newpassword,website))
                    sqliteConnection.commit()
                    print("Updated the table")
                    cursor.execute("SELECT * FROM password where =?",(website))
                    rows = cursor.fetchall()
                    print(rows)
            else:
                print("No update was done this is the current details",select_func(website))        


        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            #  cursor.execute("SELECT * FROM password WHERE priority=?", (priority,))        


## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## length of password from the user
	length = int(input("Enter password length: "))

	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)
    
	## converting the list to string
	## printing the list
	return "".join(password)
        



## invoking the function

# print("For opening the vault ")
# val = input("Enter the website:")
# val = input("Enter the password")
# insert_func('rahulpoolanchalil@gmail.com', generate_random_password())
  
while True:

    user_input =int(input("""=======Please enter you input========
    1. Retrieve password
    2. Insert new Entry 
    3. quit
     """))

    # print("userinput:",user_input)
    if user_input == 1:
        website = input("Enter the website: ")
        select_func(website)
    elif user_input == 2:
        website = input("Enter the website: ")
        
        newpassword=str(generate_random_password())
        # print("newpas:",newpassword)
        insert_func(website, newpassword)      
    elif user_input == 3:
        print("Exiting the programme")
        break

# print(user_input)