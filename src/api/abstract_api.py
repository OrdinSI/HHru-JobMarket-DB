from abc import ABC, abstractmethod


class Api(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def get_vacancies(self, request):
        """Получение вакансий с разных платформ"""
        pass


    @abstractmethod
    def get_id_employers(self, request):
        """Получение id компаний с разных платформ"""
        pass