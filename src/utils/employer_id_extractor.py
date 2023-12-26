from typing import Any, Dict


def extract_employer_id(data: Dict[str, Any]) -> int:
    """Функция для извлечения id компании из запроса"""
    items = data.get('items', [])
    if items and isinstance(items, list) and isinstance(items[0], dict):
        employer_id = items[0].get('id', '')
        if employer_id.isdigit():
            return int(employer_id)
    return 0
