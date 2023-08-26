import sys
import pandas as pd

from utils import count_pages


def show(phone_book: pd.DataFrame, page_number: int, page_size: int) -> None:
    """Выводит указанную страницу справочника"""

    # Проверка на наличие указанной страницы в словаре
    pages_in_book: int = count_pages(phone_book, page_size)
    if page_number > pages_in_book:
        print(f"Страницы {page_number} нет в словаре")
        sys.exit(1)

    # Определяем индексы первой и последней строк на странице
    start_index: int = (page_number - 1) * page_size
    end_index: int = start_index + page_size

    # Выводим указанную страницу справочника и подпись
    display(phone_book[start_index:end_index])
    print(f"\nСтраница {page_number} из {pages_in_book}")


def search(phone_book: pd.DataFrame, search_parameters: dict[str, str]) -> pd.DataFrame:
    """Осуществляет поиск записей в справочнике по указанным параметрам"""

    search_result: pd.DataFrame = phone_book

    for column, value in search_parameters.items():
        if value:
            search_result = search_result[search_result[column] == value]

    return search_result


def add(phone_book: pd.DataFrame, record_fields: dict[str, str]) -> pd.DataFrame:
    """Добавляет запись в справочник и возвращает его"""

    new_record: pd.DataFrame = pd.DataFrame.from_dict([record_fields])

    if len(search(phone_book, record_fields)) != 0:
        print("Такая запись уже есть в справочнике")
        return phone_book

    new_phone_book: pd.DataFrame = pd.concat(
        [phone_book, new_record], ignore_index=True
    )

    return new_phone_book


def edit(
    phone_book: pd.DataFrame, index: int, fields_to_edit: dict[str, str]
) -> pd.DataFrame:
    """Редактирует запись в справочнике и возвращает обновлённый справочник"""

    if len(phone_book) < index:
        print("Такой записи нет в справочнике")
        return phone_book

    for column, value in fields_to_edit.items():
        if value:
            phone_book.loc[index, column] = value

    return phone_book


def display(phone_book: pd.DataFrame) -> None:
    """Печатает в терминал переданный датафрейм"""

    print(phone_book.to_string())


def save(phone_book: pd.DataFrame, path: str) -> None:
    """Сохраняет справочник в формате CSV по указанному пути"""

    phone_book.to_csv(path, index=False)
