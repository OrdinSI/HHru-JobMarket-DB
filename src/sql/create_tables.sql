-- Создание базы(либо через pgAdmin)
CREATE DATABASE job_market_hh
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'ru_RU.UTF-8'
    LC_CTYPE = 'ru_RU.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Таблица с данными о компаниях
CREATE TABLE employers
(
    employers_id varchar(100) PRIMARY KEY,
    name varchar(255) NOT NULL,
    url varchar(255),
    vacancies_url varchar(255) NOT NULL,
    open_vacancies int NOT NULL
);

-- Таблица с данными о вакансиях
CREATE TABLE vacancies
(
    vacancies_id varchar(100) PRIMARY KEY,
    employers_id varchar(100) REFERENCES employers(employers_id) NOT NULL,
    name varchar(255) NOT NULL,
    salary int NOT NULL,
    requirement text,
    responsibility text,
    area varchar(255),
    url varchar(255)
);

