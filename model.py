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

#let the database match for us. If the pair matches then return ID else return (ID number)-1 (False)
def authenticate(username, password):
    query = """SELECT id FROM Users WHERE username = ? AND password = ?"""
    DB.execute(query, (username, password))
    row = DB.fetchone()
# If a row matches 
    if row:       
        return row[0]
    else:
        return -1

def create_new_account(username, password):
    print "Create account with user, pwd",username, password
    query = """INSERT INTO Users (username, password) VALUES (?, ?)"""
    DB.execute(query, (username, password))
    CONN.commit()
#TODO check for failure before blinding returning true. 
    return True 
 

def user_exists(username):
    print "We made it to the user existence checker with user name ", username

    query = """SELECT id FROM Users WHERE username = ?"""
    DB.execute(query, (username,))
    row = DB.fetchone()

    print dir(row)

    if row:
        return True
    else:
        return False