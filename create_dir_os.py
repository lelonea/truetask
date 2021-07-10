import os
from saver import *
from datetime import datetime


unique_dates_not_sorted = list(set(dates))
unique_dates = sorted(unique_dates_not_sorted)
months = []

RU_MONTH_VALUES = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12,
}


def int_value_from_ru_month(date_str):
    """
    Заменяет русское название месяца на его номер
    :param date_str: дата типа (5 Июля) в формате str
    :return: дата типа (5 7) в формате str
    """
    for k, v in RU_MONTH_VALUES.items():
        date_str = date_str.replace(k, str(v))
    return date_str


def find_month_name(date_name):
    """
    Определяет имя месяца на английском
    :param date_name: дата типа (5 Июля) в формате str
    :return: название месяца на английском типа (JULY) в формате str
    """
    reform = int_value_from_ru_month((str(date_name)).lower())
    format_date = datetime.strptime(reform, '%d %m')
    return format_date.strftime('%B')


def index_in_img(date_name):
    """
    Определяет индексы даты в листе dates,
    соответствующих им названий праздников в листе titles
    и ссылок на открытки в листе card_urls
    :param date_name: дата типа (5 Июля) в формате str
    :return: list индексов типа [1, 5]
    """
    return [index for index, value in enumerate(dates) if value == date_name]


def create_month_dir(month_list):
    """
    Создаёт папки с названиями месяцев на английском типа (JULY)
    :param month_list: Уникальные названия месяцев в листе (list)
    :return: None
    """
    for month in month_list:
        os.mkdir(month)


def create_date_dir(date_list):
    """
    Создаёт папки с названиями дат типа (5 июля)
    :param date_list: Уникальные названия дат в листе (list)
    :return: None
    """
    for date_name in date_list:
        os.chdir(find_month_name(date_name))
        os.mkdir(date_name)
        os.chdir('..')


def create_holiday_dir_with_img(date_list):
    """
    Создаёт папки с названиями праздников и сохраняет в них соответствующие файлы
    :param date_list: Уникальные названия дат в листе (list)
    :return: None
    """
    for date_name in date_list:
        os.chdir(find_month_name(date_name))
        os.chdir(date_name)
        for holiday in index_in_img(date_name):
            os.mkdir(titles[holiday])
            os.chdir(titles[holiday])
            save_imgs(holiday)
            print('//')
            os.chdir('..')
        os.chdir('../..')


def del_empty_dirs(path):
    """
    Удаляет пустые папки в случае если такие образовались из-за присутствия в открытках только видео-формата
    Рекурсивная функция проходится по всем папкам начиная с директории path
    При удалении папки выводит в командной строке название удалённой папки
    :param path: Путь
    :return: None
    """
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)
                print(a, 'удалена')


for dates_name in unique_dates:
    months.append(find_month_name(dates_name))

unique_month = list(set(months))


def run():
    """
    Создаёт в текущей директории с проектом папки и загружает файлы
    После загрузки удаляет пустые папки
    Архитектура: Месяц - Дата - Праздник - Открытки
    :return: None
    """
    create_month_dir(unique_month)
    create_date_dir(unique_dates)
    create_holiday_dir_with_img(unique_dates)
    del_empty_dirs(os.curdir)
    print('End')
