import logging
from typing import Any, Dict, List
import time
import requests

from src.api.abstract_api import Api
from src.utils.config import per_page


class HeadHunterApi(Api):
    """Класс для работы с API HeadHunter"""

    def get_vacancies(self, requests_v: List[str]) -> Dict[str, Any]:
        """Получение вакансий с HeadHunter по запросу"""
        vacancies = {}
        try:
            for request in requests_v:
                params = dict(per_page=per_page, only_with_salary=True)
                res = requests.get(request, params=params)
                if res.ok:
                    vacancies[request] = res.json()
                    time.sleep(1)
                else:
                    logging.error(f"Запрос {request} вернул статус {res.status_code}")
            return vacancies
        except Exception as e:
            logging.error(f"Ошибка при получении вакансий с HeadHunter: {e}")

    def get_employer(self, request: str) -> Dict[str, Any]:
        """Получение id компаний с HeadHunter по запросу"""
        try:
            params = dict(text=request, only_with_vacancies=True)
            res = requests.get('https://api.hh.ru/employers', params=params)
            return res.json()
        except Exception as e:
            logging.error(f"Ошибка при получении id компаний с HeadHunter: {e}")
