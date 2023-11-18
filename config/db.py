import psycopg2
from dotenv import load_dotenv
import os


from db.crud import anime_table, manga_table

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
)


cursor = conn.cursor()
cursor.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")


def create_tables():
    cursor.execute(anime_table)
    cursor.execute(manga_table)
    conn.commit()
