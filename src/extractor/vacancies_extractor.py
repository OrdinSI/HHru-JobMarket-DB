from src.extractor.abstract_extractor import Extractor


class VacanciesExtractor(Extractor):
    def __init__(self):
        self.vacancies = {}

    def extract_data(self, datas):
        for data in datas.get('items', []):
            if data and isinstance(data, dict):
                vacancies_id = data.get('id')
                employer_id = data.get('employer').get('id')
                vacancies_name = data.get('name', '')
                vacancies_salary = data.get('salary').get('from', 0)
                vacancies_requirement = data.get('snippet').get('requirements', '')
                vacancies_responsibility = data.get('snippet').get('responsibility', '')
                vacancies_area = data.get('area').get('name', '')
                vacancies_url = data.get('alternate_url', '')
                self.vacancies[vacancies_id] = {
                    'employer_id': employer_id,
                    'name': vacancies_name,
                    'salary': vacancies_salary,
                    'requirements': vacancies_requirement,
                    'responsibility': vacancies_responsibility,
                    'area': vacancies_area,
                    'url': vacancies_url
                }

        return self.vacancies


    def get_data(self):
        pass




