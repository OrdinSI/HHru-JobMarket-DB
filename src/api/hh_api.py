from typing import Any, Dict
import requests
from src.api.abstract_api import Api
import logging


class HeadHunterApi(Api):
    """Класс для работы с API HeadHunter"""

    def get_vacancies(self, request: str) -> Dict[str, Any]:
        """Получение вакансий с HeadHunter по запросу"""
        try:
            params = dict(text=request)
            res = requests.get('https://api.hh.ru/vacancies', params=params)
            return res.json()
        except Exception as e:
            logging.error(f"Ошибка при получении вакансий с HeadHunter: {e}")