"""
SQLITE BASICS — Python Fundamentals

SQLite is a lightweight database included with Python.
Useful 5.1 - For small apps, prototypes, and local storage.
"""

import sqlite3

# ---------------------------------------------------------
# CONNECTING TO A DATABASE
# ---------------------------------------------------------

connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# ---------------------------------------------------------
# CREATING A TABLE
# ---------------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

# ---------------------------------------------------------
# INSERTING DATA
# ---------------------------------------------------------

cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", ("Marlon", 31))
connection.commit()

# ---------------------------------------------------------
# READING DATA
# ---------------------------------------------------------

cursor.execute("SELECT * FROM people")
rows = cursor.fetchall()
print(rows)

# ---------------------------------------------------------
# CLEANUP
# ---------------------------------------------------------

connection.close()
