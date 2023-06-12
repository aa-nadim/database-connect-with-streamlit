from deta import Deta

DETA_KEY = "d0dpkbuet9f_Qs7uRPmAN7F9woZ5hg72bjfNWyTaXoWN"

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("users_db")

def insert_user(username, name, password):
    """Returns the user on a successful user creation, otherwise raises and error"""
    return db.put({"key": username, "name": name, "password": password})

insert_user("nadim", "Mr Nadim", "abc123")
