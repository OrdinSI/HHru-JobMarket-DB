import logging
from src.api.hh_api import HeadHunterApi
from src.utils.colors import Colors
from src.utils.employer_id_extractor import extract_employer_id


logging.basicConfig(
    #filename='job_explorer.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(module)s:  [%(funcName)s] %(message)s'
)


def user_interaction():
    """ Основная функция для взаимодействия с пользователем"""
    Colors.print_magenta("Привет!\nЯ представляю собой программу для анализа вакансий у конкретных работодателей")
    search_query = Colors.input_cyan("Пожалуйста, введите ваш поисковый запрос: ")

    hh_api = HeadHunterApi()
    data_employer = hh_api.get_id_employers(search_query.lower())
    if data_employer:
        employer_id = extract_employer_id(data_employer)
        if employer_id != 0:
            vacancies = hh_api.get_vacancies(employer_id)
        else:
            Colors.print_red("К сожалению не возможно получить информацию о данной компании")
    else:
        Colors.print_red("К сожалению данной компании на HeadHunter не найдено")






if __name__ == "__main__":
    user_interaction()