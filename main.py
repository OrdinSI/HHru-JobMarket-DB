import logging
import os
import psycopg2
from dotenv import load_dotenv
from src.api.hh_api import HeadHunterApi
from src.utils.colors import Colors
from src.extractor.employers_extractor import EmployersExtractor
from src.extractor.vacancies_extractor import VacanciesExtractor



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
    data_employer = hh_api.get_employer(search_query.lower())

    if data_employer:
        employers_extractor = EmployersExtractor()
        employers = employers_extractor.extract_data(data_employer)
        if employers:
            vacancies_url = employers_extractor.get_employer_vacancies_url()
            vacancies_data = hh_api.get_vacancies(vacancies_url)
            print(vacancies_data)
            # if vacancies_data:
            #     vacancies_extractor = VacanciesExtractor()
            #     vacancies = vacancies_extractor.extract_data(vacancies_data)


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

