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
    for k, v in RU_MONTH_VALUES.items():
        date_str = date_str.replace(k, str(v))
    return date_str


def find_month_name(date_name):
    reform = int_value_from_ru_month((str(date_name)).lower())
    format_date = datetime.strptime(reform, '%d %m')
    return format_date.strftime('%B')


def index_in_img(date_name):
    return [index for index, value in enumerate(dates) if value == date_name]


def index_in_dates(date_name):
    return dates.index(date_name)


def create_month_dir(month_list):
    for month in month_list:
        os.mkdir(month)


def create_date_dir(date_list):
    for date_name in date_list:
        os.chdir(find_month_name(date_name))
        os.mkdir(date_name)
        os.chdir('..')


def create_holiday_dir_with_img(date_list):
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
    create_month_dir(unique_month)
    create_date_dir(unique_dates)
    create_holiday_dir_with_img(unique_dates)
    del_empty_dirs(os.curdir)
    print('End')

