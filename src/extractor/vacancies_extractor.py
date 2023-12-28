from src.extractor.abstract_extractor import Extractor


class VacanciesExtractor(Extractor):
    def __init__(self):
        self.vacancies = {}

    def extract_data(self, datas):
        """Функция для извлечения данных вакансий компании из запроса"""
        for request, data in datas.items():
            items = data.get('items', [])
            for item in items:
                if item and isinstance(item, dict):
                    vacancies_id = item.get('id')
                    employer_id = item.get('employer').get('id')
                    vacancies_name = item.get('name', '')
                    vacancies_salary = item.get('salary').get('from', 0)
                    vacancies_requirement = item.get('snippet').get('requirement', '')
                    vacancies_responsibility = item.get('snippet').get('responsibility', '')
                    vacancies_area = item.get('area').get('name', '')
                    vacancies_url = item.get('alternate_url', '')
                    self.vacancies[vacancies_id] = {
                        'employers_id': employer_id,
                        'name': vacancies_name,
                        'salary': vacancies_salary,
                        'requirement': vacancies_requirement,
                        'responsibility': vacancies_responsibility,
                        'area': vacancies_area,
                        'url': vacancies_url
                    }

        return self.vacancies






