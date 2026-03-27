import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    amount INTEGER,
    month TEXT
)
""")

cursor.executemany("""
INSERT INTO sales (product, amount, month)
VALUES (?, ?, ?)
""", [
    ("Laptop", 50000, "Jan"),
    ("Mobile", 20000, "Jan"),
    ("Laptop", 60000, "Feb"),
    ("Mobile", 25000, "Feb"),
])

conn.commit()
conn.close()
