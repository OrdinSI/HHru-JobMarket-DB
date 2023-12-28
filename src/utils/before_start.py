import logging
import os
import psycopg2
from dotenv import load_dotenv
from src.api.hh_api import HeadHunterApi
from src.db.db_save import DBSave
from src.extractor.employers_extractor import EmployersExtractor
from src.extractor.vacancies_extractor import VacanciesExtractor
from src.utils.config import employers


def connect_to_db():
    """Подключение к PostgreSQL"""
    load_dotenv()
    return psycopg2.connect(host=os.getenv('POSTGRES_HOST', default="localhost"),
                            port=os.getenv('POSTGRES_PORT', default="5432"),
                            database=os.getenv('POSTGRES_DB', default="postgres"),
                            user=os.getenv('POSTGRES_USER', default="postgres"),
                            password=os.getenv('POSTGRES_PASSWORD', default=""))


def before_start(conn_db):
    try:
        save = DBSave(conn_db)
        hh_api = HeadHunterApi()
        vacancies_extractor = VacanciesExtractor()
        employers_extractor = EmployersExtractor()

        data_employer = hh_api.get_employer(employers)
        employers_data = employers_extractor.extract_data(data_employer)
        save.data_saving('employers', employers_data)

        vacancies_url = employers_extractor.get_employer_vacancies_url()
        vacancies_data = hh_api.get_vacancies(vacancies_url)
        vacancies = vacancies_extractor.extract_data(vacancies_data)
        save.data_saving("vacancies", vacancies)
    except Exception as e:
        logging.error(f"Произошла ошибка при сохранении данных: {e}")


if __name__ == "__main__":
    conn = connect_to_db()
    try:
        before_start(conn)
    finally:
        conn.close()
