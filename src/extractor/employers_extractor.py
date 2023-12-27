from src.extractor.abstract_extractor import Extractor


class EmployersExtractor(Extractor):
    def __init__(self):
        self.employers = {}

    def extract_data(self, datas):
        """Функция для извлечения данных компании из запроса"""
        for data in datas.get('items', []):
            if data and isinstance(data, dict):
                employer_id = data.get('id', '')
                employer_name = data.get('name', '')
                employer_url = data.get('alternate_url', '')
                employer_vacancies_url = data.get('vacancies_url', '')
                employer_vacancies = data.get('open_vacancies', 0)
                self.employers[employer_id] = {
                    'name': employer_name,
                    'url': employer_url,
                    'vacancies_url': employer_vacancies_url,
                    'open_vacancies': employer_vacancies
                }

        return self.employers

    def get_data(self):
        pass

    def get_employer_vacancies_url(self):
        vacancies_url = []
        for employer_id, employer_info in self.employers.items():
            if employer_info['open_vacancies'] != 0:
                vacancies_url.append(employer_info['vacancies_url'])
        return vacancies_url
