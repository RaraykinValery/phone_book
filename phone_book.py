import argparse
import pandas as pd
import os
import sys

from services import add, display, edit, save, search, show
from utils import map_arguments_to_columns


def execute_show(args: argparse.Namespace) -> None:
    """Вызывает функцию show"""

    show(args.phone_book, args.page_number, args.page_size)


def execute_search(args: argparse.Namespace) -> None:
    """Вызывает функцию search и отображает её результаты"""

    search_results: pd.DataFrame = search(
        args.phone_book, map_arguments_to_columns(args)
    )
    if len(search_results) == 0:
        print("Записи с указанными параметрами не найдены")
    else:
        print(f"Найдено записей: {len(search_results)}\n")
        display(search_results)


def execute_add(args: argparse.Namespace) -> None:
    """Вызывает функцию add и сохраняет результат её выполнения"""

    save(add(args.phone_book, map_arguments_to_columns(args)), path=args.file)


def execute_edit(args: argparse.Namespace) -> None:
    """Вызывает функцию edit и сохраняет её результаты"""

    save(edit(args.phone_book, args.id, map_arguments_to_columns(args)), path=args.file)


def main():
    # Парсинг аргументов командной строки
    file_path_parser = argparse.ArgumentParser(add_help=False)
    file_path_parser.add_argument("-fl", "--file", default="phone_book.csv")

    arguments_by_columns_parser = argparse.ArgumentParser(add_help=False)
    arguments_by_columns_parser.add_argument("-l", "--last_name", type=str)
    arguments_by_columns_parser.add_argument("-f", "--first_name", type=str)
    arguments_by_columns_parser.add_argument("-p", "--patronymic", type=str)
    arguments_by_columns_parser.add_argument("-o", "--organization", type=str)
    arguments_by_columns_parser.add_argument("-w", "--work_phone", type=str)
    arguments_by_columns_parser.add_argument("-ph", "--personal_phone", type=str)

    main_parser = argparse.ArgumentParser(
        description="Search, add, edit phone book records", parents=[file_path_parser]
    )
    main_parser.set_defaults(func=execute_show)
    main_parser.add_argument("-p", "--page_number", default=1, type=int)
    main_parser.add_argument("-s", "--page_size", default=10, type=int)

    subparsers = main_parser.add_subparsers()

    parser_search = subparsers.add_parser(
        "search", parents=[file_path_parser, arguments_by_columns_parser]
    )
    parser_search.set_defaults(func=execute_search)

    parser_edit = subparsers.add_parser(
        "edit", parents=[file_path_parser, arguments_by_columns_parser]
    )
    parser_edit.add_argument("-i", "--id", type=int, required=True)
    parser_edit.set_defaults(func=execute_edit)

    parser_add = subparsers.add_parser(
        "add", parents=[file_path_parser, arguments_by_columns_parser]
    )
    parser_add.set_defaults(func=execute_add)

    args = main_parser.parse_args()

    # Проверка существования справочника
    if os.path.isfile(args.file):
        # Загружается справочник
        phone_book: pd.DataFrame = pd.read_csv(args.file, dtype=str)
    else:
        # Создаём пустой справочник
        phone_book = pd.DataFrame(
            columns=[
                "Фамилия",
                "Имя",
                "Отчество",
                "Название организации",
                "Телефон рабочий",
                "Телефон личный (сотовый)",
            ]
        )
        save(phone_book, args.file)

    if len(phone_book) == 0:
        print("Справочник пуст")
        sys.exit(1)

    # Устанавливается начало индекса с 1, а не с 0
    phone_book.index = phone_book.index + 1

    # Добавление справочника в список аргументов
    args.phone_book = phone_book

    args.func(args)


if __name__ == "__main__":
    main()
