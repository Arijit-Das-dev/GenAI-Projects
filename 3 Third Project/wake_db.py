import mysql.connector
from datetime import datetime

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Arijitdas@12",
        database="jarvisWake"
    )
    return conn


def insert_wake(wake):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
        INSERT INTO wake_info (Wake_word, dates)
        VALUES (%s, %s)
    """

    today = datetime.now().date()   # store current date
    values = (wake, today)

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()