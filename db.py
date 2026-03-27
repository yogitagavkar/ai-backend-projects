import sqlite3

def run_sql(query: str):
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result