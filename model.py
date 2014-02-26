import sqlite3

DB = None
CONN = None

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("thewall.db")
    DB = CONN.cursor()

#change this a bit
#def get_auth_by_username(username, password):

# ADMIN_USER="hackbright"
# ADMIN_PASSWORD=5980025637247534551
#The README lied about the above.   The answer is not, in fact, 42.

def authenticate(username, password):
    query = """SELECT id FROM Users WHERE username = ? AND password = ?"""
    DB.execute(query, (username, password))
    row = DB.fetchone()
# If a row matches 
    if row:
        print row,id, row[0]        
        return row[0]
    else:
        return -1
    #get connection code
    #build the query
    #open a database connection
    # return True or False if its in the DB with coorect password
    # if true render a landing page
    # if false light the user on fire with an error! 
    #   and redirect to login page

