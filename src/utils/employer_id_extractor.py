from typing import Any, Dict


def extract_employer(datas: Dict[str, Any]) -> int:
    """Функция для извлечения id компании из запроса"""
    for data in datas.get('items', []):
        if data and isinstance(data, list) and isinstance(data[0], dict):
            employer_id = data[0].get('id', '')
            employer_name = data[0].get('name', '')
            employer_url = data[0].get('alternate_url', '')
            employer_vacancies_url = data[0].get('vacancies_url', '')
            employer_vacancies = data[0].get('open_vacancies', 0)
            if employer_id.isdigit():
                return int(employer_id)
        return 0


