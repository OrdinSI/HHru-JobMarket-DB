# import logging
# from src.api.hh_api import HeadHunterApi
#
#
# class DBSave:
#     """Класс для сохранения информации в базу"""
#
#     def __init__(self, conn, search_query):
#         self.search_query = search_query
#         self.conn = conn
#         self.cursor = self.conn.cursor()
#         self.hh_api = HeadHunterApi()
#
#     def det_api_employer(self):
#         """Получение данных employer по api hh"""
#         return self.hh_api.get_employer(self.search_query)
#
#     def get_employer(self):
#         """ Извлечение данных полученных по api"""
#         data = self.det_api_employer()
#         return extract_employer(data)
#
#     def data_saving(self):
#         """ Сохранение данных в таблицу employers"""
#         employer_id, employer_name, employer_url, employer_vacancies, employer_vacancies_url = self.get_employer()
#         if employer_id:
#             try:
#                 with self.conn:
#                     with self.conn.cursor() as cursor:
#                         cursor.execute('INSERT INTO employers VALUES (%s, %s, %s, %s)',
#                                        (employer_id, employer_name, employer_url, employer_vacancies))
#
#                 logging.info("Успешное добавление в таблицу employers.")
#                 self.save_vacancies(employer_vacancies_url)
#                 return True
#             except Exception as e:
#                 logging.error(f"Произошла ошибка при добавлении данных в таблицу employers: {e}")
#                 return False
#
#     def get_api_vacancies(self, employer_vacancies_url):
#         return self.hh_api.get_vacancies(employer_vacancies_url)
#
#     def get_vacancies(self):
#         pass
#
#     def save_vacancies(self, employer_vacancies_url):
#         data = self.hh_api.get_vacancies(employer_vacancies_url)

