import sqlite3
import bcrypt

# Database
conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
username TEXT,
password BLOB
)
""")

# Register
def register():
    username = input("Username: ")
    password = input("Password: ")

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    cur.execute(
        "INSERT INTO users VALUES(?,?)",
        (username, hashed)
    )

    conn.commit()
    print("Registration Successful")

# Login
def login():
    username = input("Username: ")
    password = input("Password: ")

    cur.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )

    user = cur.fetchone()

    if user and bcrypt.checkpw(
        password.encode(),
        user[0]
    ):
        print("Login Successful")
    else:
        print("Invalid Credentials")

while True:

    print("\n1.Register")
    print("2.Login")
    print("3.Exit")

    choice = input("Choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        break