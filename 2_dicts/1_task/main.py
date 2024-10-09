import os
from os.path import split

from decimal import Decimal

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    """Внешнее апи, которое возвращает вам список строк с данными по сотрудникам."""
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    """Функция парсит данные, полученные из внешнего API и приводит их к стандартизированному виду."""
    info = get_employees_info()
    parsed_employees_info = []

    # Ваш код ниже
    for sentence in info:
        dict = {'id': 0, 'name': 0, 'last_name': 0, 'age': 0, 'position': 0, 'salary': 0}
        split_sentence = sentence.split()
        for index in range(len(split_sentence)):
            if split_sentence[index] in ['id','age']:
                dict[split_sentence[index]] = int(split_sentence[index + 1])
            elif split_sentence[index] in ['name', 'last_name', 'position']:
                dict[split_sentence[index]] = str(split_sentence[index + 1])
            elif split_sentence[index] in 'salary':
                dict[split_sentence[index]] = Decimal(split_sentence[index + 1])
        parsed_employees_info += [dict]
    return parsed_employees_info

