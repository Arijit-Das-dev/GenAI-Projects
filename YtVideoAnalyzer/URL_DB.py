import mysql.connector
from datetime import datetime

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Arijitdas@12",
        database="URLDB"
    )
    return conn


def insert_url(url):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
        INSERT INTO url_info (url, date)
        VALUES (%s, %s)
    """

    today = datetime.now().date()   # store current date
    values = (url, today)

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()