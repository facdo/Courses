# Section 15 - Python for Interacting with SQLite and PostgreSQL Databases
# 122 - Introduction to Working with Databases
# Organize, store and search information in databases such as: PostgreSQL,
# Oracle and SQLite
# How to interact with these databases using python
# In SQLite all the information to access and search the database is in the .db
# file. So it is interesting for portabilitiy
# For PostgreSQL the data is stored in the web
# We are going to need two libraries for working with those databases:
# sqlite3 and psycopg2

# 123 - Connecting and Inserting data to SQLite via Python

# using this library enables us to write SQL code inside python.
import sqlite3

# there are basically 5 steps in working with databases
# 1 - Connect to a database
# 2 - Create a cursor objects that points to some row in the connected database
# 3 - Write an SQL query, so we can insert or retrieve data from our database
# 4 - Commit changes to the database
# 5 - Close the connection with the database

# # start our connection with a database file
# # we store the connection object in a variable
# # if the specified file doesn't exists it will be created with this line
# conn=sqlite3.connect("lite.db")
# # then we have to create a cursor for pointing somewhere in our connection object
# cur=conn.cursor()
# # now we can execute SQL commands from the cursor object, using the execute method
# # note that SQL code is ALWAYS inside double quotes "", as a string input to the
# # execute method
# # Our database is empty, so the first thing is to create a table with a relevant
# # name and the column names and variable types associated to it
# # note that REAL is equivalent to float
# # to avoid errors when running the code multiple times the creation of the table
# # is conditioned to its existence
# cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
# # now lets insert some data into it
# cur.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.5)")
# # to add more items we should use a function to add new itens to our database,
# # otherwise we might have duplicate itens being inserted
# # the next step is to commit our changes and them close the connection
# conn.commit()
# conn.close()

# so lets modify everything to get it all inside functions

def create_table():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    # to pass the function arguments to the sql command we use ? syntax, and
    # then pass the variables as a separate argument for the method execute
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()

# the next step would be to visualize the information stored in the sql database
# so lets create a function to do that
def view():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    # lets say we want to select the data from all the columns in our database
    # * means all
    cur.execute("SELECT * FROM store")
    # so, after the data is selected we want to get it and save-it in a python
    # variable
    rows=cur.fetchall()
    # we don't need to commit because we are only selecting the data
    conn.close()
    return rows


# 124 - Selecting, Inserting, Deleting and Updating SQLite databases

# update and delete functions
def delete(item):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

# update
def update(item, quantity, price):
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
                (quantity, price, item))
    conn.commit()
    conn.close()

# # We can call the function insert and pass the information as arguments
#insert("Coffe Cup", 10, 8.0)

# lets test our delete funtion
# delete('Wine Glass')
# and our uptdate function
# update("Coffe Cup", 23, 11.0)
print(view())
