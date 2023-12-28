import logging
import os
import psycopg2
from dotenv import load_dotenv


def connect_to_db():
    """Подключение к PostgreSQL"""
    load_dotenv()
    return psycopg2.connect(host=os.getenv('POSTGRES_HOST', default="localhost"),
                            port=os.getenv('POSTGRES_PORT', default="5432"),
                            database=os.getenv('POSTGRES_DB', default="postgres"),
                            user=os.getenv('POSTGRES_USER', default="postgres"),
                            password=os.getenv('POSTGRES_PASSWORD', default=""))


def create_tables(conn_db):
    """Создание таблиц в базе данных"""
    try:
        with conn_db:
            with conn_db.cursor() as cursor:
                with open('./create_tables.sql') as f:
                    sql_script = f.read()
                cursor.execute(sql_script)

    except Exception as e:
        logging.error(f"Произошла ошибка при создании таблиц: {e}")


if __name__ == "__main__":
    conn = connect_to_db()
    try:
        create_tables(conn)
    finally:
        conn.close()
