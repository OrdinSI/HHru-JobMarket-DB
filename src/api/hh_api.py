import logging
from typing import Any, Dict
import requests
from src.api.abstract_api import Api
from src.utils.config import per_page


class HeadHunterApi(Api):
    """Класс для работы с API HeadHunter"""
    def get_vacancies(self, request: int) -> Dict[str, Any]:
        """Получение вакансий с HeadHunter по запросу"""
        try:
            params = dict(employer_id=request, per_page=per_page)
            res = requests.get('https://api.hh.ru/vacancies', params=params)
            return res.json()
        except Exception as e:
            logging.error(f"Ошибка при получении вакансий с HeadHunter: {e}")

    def get_id_employers(self, request: str) -> Dict[str, Any]:
        """Получение id компаний с HeadHunter по запросу"""
        try:
            params = dict(text=request)
            res = requests.get('https://api.hh.ru/employers', params=params)
            return res.json()
        except Exception as e:
            logging.error(f"Ошибка при получении id компаний с HeadHunter: {e}")
