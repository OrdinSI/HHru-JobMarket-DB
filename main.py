import logging
import os
import psycopg2
from dotenv import load_dotenv
from src.api.hh_api import HeadHunterApi
from src.utils.colors import Colors
from src.utils.employer_id_extractor import extract_employer_id
from src.db.db_save import DBSave




logging.basicConfig(
    #filename='job_explorer.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(module)s:  [%(funcName)s] %(message)s'
)


def connect_to_db():
    """Подключение к PostgreSQL"""
    load_dotenv()
    return psycopg2.connect(host=os.getenv('POSTGRES_HOST', default="localhost"),
                            port=os.getenv('POSTGRES_PORT', default="5432"),
                            database=os.getenv('POSTGRES_DB', default="postgres"),
                            user=os.getenv('POSTGRES_USER', default="postgres"),
                            password=os.getenv('POSTGRES_PASSWORD', default=""))


def user_interaction(conn_db):
    """ Основная функция для взаимодействия с пользователем"""
    Colors.print_magenta("Привет!\nЯ представляю собой программу для анализа вакансий у конкретных работодателей")
    search_query = Colors.input_cyan("Пожалуйста, введите ваш поисковый запрос: ")

    hh_api = HeadHunterApi()
    data_employer = hh_api.get_id_employers(search_query.lower())
    if data_employer:
        db_save = DBSave(conn_db)
        db_save.data_saving(data_employer)
        employer_id = extract_employer_id(data_employer)
        if employer_id != 0:
            vacancies = hh_api.get_vacancies(employer_id)
        else:
            Colors.print_red("К сожалению не возможно получить информацию о данной компании")
    else:
        Colors.print_red("К сожалению данной компании на HeadHunter не найдено")


if __name__ == "__main__":
    conn = connect_to_db()
    try:
        user_interaction(conn)
    finally:
        conn.close()

