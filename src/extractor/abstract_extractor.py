from abc import ABC, abstractmethod


class Extractor(ABC):
    """Абстрактный класс для работы с данными"""
    @abstractmethod
    def extract_data(self, datas):
        pass
