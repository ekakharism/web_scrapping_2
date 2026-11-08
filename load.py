import psycopg
import os 
from dotenv import load_dotenv

load_dotenv()

def save_data(hasil):
    conn = psycopg.connect(
        host=os.getenv("DB_HOST"), 
        user=os.getenv("DB_USER"), 
        password=os.getenv("DB_PASSWORD"), 
        dbname=os.getenv("DB_NAME"), 
        port=os.getenv("DB_PORT")
    )

    cur = conn.cursor()

    cur.execute("""
        create table if not exists books(
        id serial primary key,
        title text,
        price text,
        rating int,
        status_stok text,
        link text
        )
    """)

    with cur.copy("COPY books(title,price,rating,status_stok,link)from STDIN") as copy:
        for row in hasil.values.tolist():
            copy.write_row(row)

    conn.commit()
    conn.close()

