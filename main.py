import logging
import os

import psycopg2
from dotenv import load_dotenv

from src.api.hh_api import HeadHunterApi
from src.db.db_manager import DBManager
from src.db.db_save import DBSave
from src.extractor.employers_extractor import EmployersExtractor
from src.extractor.vacancies_extractor import VacanciesExtractor
from src.utils.colors import Colors
from src.utils.messages import *

logging.basicConfig(
    # filename='job_explorer.log',
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

    Colors.print_magenta(GREETING)

    while True:

        db_manager = DBManager(conn_db)

        Colors.print_magenta(PRINT_CHOICE)
        choice = Colors.input_cyan(INPUT_CHOICE)

        if choice == "1":
            # Выводим список компаний
            employers_names = db_manager.get_companies()
            Colors.print_magenta(LIST_EMPLOYERS.format(employers_names))
            continue

        if choice == "2":
            # Добавление компаний
            search_query = Colors.input_cyan(ADD_EMPLOYER)
            request_e = search_query.lower().split()
            hh_api = HeadHunterApi()
            data_employer = hh_api.get_employer(request_e)
            if not data_employer:
                Colors.print_red(NONE_EMPLOYER)
                continue

            employers_extractor = EmployersExtractor()
            employers = employers_extractor.extract_data(data_employer)
            if not employers:
                Colors.print_red(ERROR_ADD_EMPLOYER)
                continue

            save = DBSave(conn_db)
            save_employers = save.data_saving("employers", employers)
            if not save_employers:
                Colors.print_red(ERROR_ADD_EMPLOYER)
                continue

            vacancies_url = employers_extractor.get_employer_vacancies_url()
            vacancies_data = hh_api.get_vacancies(vacancies_url)
            if not vacancies_data:
                Colors.print_red(NONE_VACANCIES)
                continue

            vacancies_extractor = VacanciesExtractor()
            vacancies = vacancies_extractor.extract_data(vacancies_data)
            if not vacancies:
                Colors.print_red(ERROR_ADD_VACANCIES)
                continue

            save_vacancies = save.data_saving("vacancies", vacancies)
            if not save_vacancies:
                Colors.print_red(ERROR_ADD_VACANCIES)
                continue

            Colors.print_magenta(ADD_SUCCESS)
            continue

        if choice == "3":
            open_vacancies = db_manager.get_companies_and_vacancies_count()
            Colors.print_magenta(LIST_EMPLOYERS_OPEN_VACANCIES.format(open_vacancies))
            continue

        if choice == "4":
            vacancies_data = db_manager.get_all_vacancies()
            Colors.print_magenta(ALL_VACANCIES.format(vacancies_data))
            continue

        if choice == "5":
            avg_salary = db_manager.get_avg_salary()
            Colors.print_magenta(AVG_SALARY.format(avg_salary))
            continue

        if choice == "6":
            avg_vacancies = db_manager.get_vacancies_with_higher_salary()
            Colors.print_magenta(AVG_VACANCIES.format(avg_vacancies))
            continue

        if choice == "7":
            keyword = Colors.input_cyan("Пожалуйста, введите ваш поисковый запрос: ")
            name_vacancies = db_manager.get_vacancies_with_keyword(keyword)
            Colors.print_magenta(VACANCIES_KEYWORD.format(name_vacancies))
            continue

        if choice == "8":
            Colors.print_magenta(GOODBYE_MESSAGE)
            break


if __name__ == "__main__":
    conn = connect_to_db()
    try:
        user_interaction(conn)
    finally:
        conn.close()
