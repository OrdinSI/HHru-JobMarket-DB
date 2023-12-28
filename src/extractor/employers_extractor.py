from src.extractor.abstract_extractor import Extractor


class EmployersExtractor(Extractor):
    def __init__(self):
        self.employers = {}

    def extract_data(self, datas):
        """Функция для извлечения данных компании из запроса"""
        for request, data in datas.items():
            items = data.get('items', [])
            for item in items:
                if item and isinstance(item, dict):
                    employer_id = item.get('id')
                    employer_name = item.get('name')
                    employer_url = item.get('alternate_url', '')
                    employer_vacancies_url = item.get('vacancies_url')
                    employer_vacancies = item.get('open_vacancies', 0)
                    self.employers[employer_id] = {
                        'name': employer_name,
                        'url': employer_url,
                        'vacancies_url': employer_vacancies_url,
                        'open_vacancies': employer_vacancies
                    }

        return self.employers

    def get_employer_vacancies_url(self):
        """Функция для извлечения данных url для запроса"""
        vacancies_url = []
        for employer_id, employer_info in self.employers.items():
            if employer_info['open_vacancies'] != 0:
                vacancies_url.append(employer_info['vacancies_url'])
        return vacancies_url
