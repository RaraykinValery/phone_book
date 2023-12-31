# Телефонный справочник

Это консольное приложение для управления телефонным справочником. Его можно использовать для добавления, редактирования, поиска и отображения записей в справочнике.

# Установка
- Склонируйте репозиторий:
```sh
git clone https://github.com/RaraykinValery/phone_book.git
```
- Перейдите в папку с проектом:
```sh
cd phone_book
```
- Установите зависимости из файла `requirements.txt`:
```bash
pip install -r requirements.txt
```

# Использование
Запустите файл phone_book.py с необходимыми аргументами, например:
```bash
python phone_book.py -p 2
```
Эта команда отобразит вторую страницу справочника.

# Доступные команды
- `search`: Осуществляет поиск записей по заданным параметрам.
- `add`: Добавляет новую запись в справочник.
- `edit`: Редактирует существующую запись в справочнике.
- без указания команды: Отображает указанную страницу справочника.

Поля которые будут искаться, добавляться или редактироваться указываются через аргументы командной строки, которые одинаковы для каждой команды.
Например, данная команда будет искать записи по фамилии Петров:
```sh
python phone_book.py search --last_name Петров
```
А следующая команда изменит фамилию у записи с индексом 5 на Петров, а имя на Иван:
```sh
python phone_book.py edit --index 5 --first_name Иван --last_name Петров
```
Следующая команда добавит в справочник запись с фамилией Бабочкин и личным номером 89034508243:
```sh
python phone_book.py add --last_name Бабочкин --personal_phone 89034508243
```

Так же ключи аргументов можно указывать в сокращённом формате, например -f вместо --first_name.
Все аргументы каждой команды можно посмотреть, указав флаг -h при вызове команды.

# Примечания
Все записи справочника по-умолчанию сохраняются в файле phone_book.csv.
Если файл phone_book.csv отсутствует в корневой директории проекта, то он будет автоматически создан при первом запуске.
Также через аргумент --file можно указать другой путь к файлу справочника.

## Требования
- Python 3.x
- Pandas
