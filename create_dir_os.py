import os
from saver import *
from datetime import datetime


unique_dates = list(set(dates))
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


def index_in_dates(date_name):
    return [index for index, value in enumerate(dates) if value == date_name]


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
        for date_ind in index_in_dates(date_name):
            os.chdir(find_month_name(date_name))
            os.chdir(date_name)
            os.mkdir(titles[date_ind])
            os.chdir(titles[date_ind])
            save_imgs(date_ind)
            print('//')
            os.chdir('../../..')


for dates_name in unique_dates:
    months.append(find_month_name(dates_name))

unique_month = list(set(months))

create_month_dir(unique_month)
create_date_dir(unique_dates)
create_holiday_dir_with_img(unique_dates)


