import logging


class DBManager:
    """ Класс для работы с БД PostgreSQL"""

    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """ Получает список всех компаний и количество вакансий у каждой компании."""
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    cursor.execute('SELECT name, open_vacancies  FROM employers')
                    rows = cursor.fetchall()
                    return rows
        except Exception as e:
            logging.error(f"Произошла ошибка при получении списка вакансий: {e}")



    def get_all_vacancies(self):
        """ Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    cursor.execute("""
                                    SELECT e.name AS employer_name, v.name AS vacancy_name, v.salary, v.url
                                    FROM vacancies AS v
                                    JOIN employers AS e ON v.employers_id = e.employers_id
                                    """)
                    rows = cursor.fetchall()
                    return rows
        except Exception as e:
            logging.error(f"Произошла ошибка при получении списка всех вакансий: {e}")

    def get_avg_salary(self):
        """ Получает среднюю зарплату по вакансиям."""
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    cursor.execute('SELECT AVG(salary)  FROM vacancies')
                    rows = cursor.fetchall()
                    return rows
        except Exception as e:
            logging.error(f"Произошла ошибка при получении среднюю зарплаты по вакансиям: {e}")

    def get_vacancies_with_higher_salary(self):
        """ Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    cursor.execute('SELECT name FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies)')
                    rows = cursor.fetchall()
                    return rows
        except Exception as e:
            logging.error(f"Произошла ошибка при получении списка всех вакансий у которых зарплата выше средней: {e}")

    def get_vacancies_with_keyword(self, keyword: str):
        """ Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    query = "SELECT name, url FROM vacancies WHERE name LIKE %s"
                    formatted_keyword = f"%{keyword}%"
                    cursor.execute(query, (formatted_keyword,))
                    rows = cursor.fetchall()
                    return rows
        except Exception as e:
            logging.error(f"Произошла ошибка при получении списка вакансий с ключевым словом '{keyword}': {e}")

    def get_companies(self):
        """ Получает список всех компаний"""
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    cursor.execute('SELECT name FROM employers')
                    rows = cursor.fetchall()
                    return rows
        except Exception as e:
            logging.error(f"Произошла ошибка при получении списка всех компаний: {e}")

