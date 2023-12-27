import logging
from typing import Dict, Any


class DBSave:
    """Класс для сохранения информации в базу"""

    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def data_saving(self, table_name: str, data_dict: Dict[str, Any]) -> bool:
        """ Сохранение данных """
        try:
            for record_id, record_data in data_dict.items():
                record_data_with_id = {f'{table_name}_id': record_id, **record_data}
                columns = list(record_data_with_id.keys())
                values = list(record_data_with_id.values())
                placeholders = ','.join(['%s'] * len(values))
                columns_formatted = ', '.join(columns)
                query = f'''INSERT INTO {table_name} ({columns_formatted})
                            VALUES ({placeholders})
                            ON CONFLICT ({table_name}_id) DO NOTHING'''
                with self.conn:
                    with self.conn.cursor() as cursor:
                        cursor.execute(query, values)
                logging.info("Успешное добавление в таблицу employers.")
                return True
        except Exception as e:
            logging.error(f"Произошла ошибка при добавлении данных в таблицу employers: {e}")
            return False
