import argparse
import pandas as pd
import math


def add_arguments_by_columns(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("-l", "--last_name", type=str)
    parser.add_argument("-f", "--first_name", type=str)
    parser.add_argument("-p", "--patronymic", type=str)
    parser.add_argument("-o", "--organization", type=str)
    parser.add_argument("-w", "--work_phone", type=str)
    parser.add_argument("-ph", "--personal_phone", type=str)


def count_pages(df: pd.DataFrame, page_size: int) -> int:
    """Считает количество страниц в справочнике в соответствии с размером страницы"""
    return math.ceil(len(df) / page_size)


def map_arguments_to_columns(args: argparse.Namespace) -> dict[str, str]:
    """Преобразует аргументы командной строки в соответствующие имена столбцов"""

    map = {
        "Фамилия": args.last_name,
        "Имя": args.first_name,
        "Отчество": args.patronymic,
        "Название организации": args.organization,
        "Телефон рабочий": args.work_phone,
        "Телефон личный (сотовый)": args.personal_phone,
    }

    return map
