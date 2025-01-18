# Banking operations widget
## Описание проекта
Программа создана для фильтрации, генерации и сортировки банковских карт и счетов, по дате и оплате.
## Зависимости проекта:
* The program uses the version Python 3.13
* flake8 = "^7.1.1"
* black = "^24.10.0"
* isort = "^5.13.2"
* mypy = "^1.13.0"
## Модули
1. Модуль widget принимает наименование карты или счет и номер и возвращает замаскированный номер
2. Модуль processing принимает список операций и возвращает отсортированные по успешности и по дате списки
3. Модуль generators сортирует списки операций и генерирует номера карт
4. Модуль decorators автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки
5. Модуль utils принимает путь к JSON файлу и возвращает список словарей с транзакциями
6. Модуль transactions_excel_csv считывает финансовые операции из Excel и SCV файлов
7. Модуль filter_banking_operations фильтрует список операций по описанию и считает количество операций по каждой категории
8. Модуль main запускает программу
## Функции, которые мы будем использовать:
* Функция скрывающая номер карты и счета - `mask_account_card`
* Функция сортировки по дате - `sort_by_date`
* Функция фильтрации в операциях по счетам - `filter_by_state`
* Функция выдающая список транзакций в определенной валюте -`filter_by_currency`
* Функция выдающая описание операций - `transaction_descriptions`
* Функция генерирующая номера карт - `card_number_generator`
* Функция принимающая JSON файл и возвращает список словарей - `load_transactions_from_json`
* Функция принимает на вход транзакцию и возвращает сумму в рублях - `transaction_amount`
* Функция для считывания финансовых операций из Excel-файла, выдает список словарей с транзакциями - `read_transactions_excel`
* Функция для считывания финансовых операций из CSV-файла, выдает список словарей с транзакциями - `read_transactions_csv`
* Функция принимает список словарей с данными о банковских операциях и строку поиска,
а возвращает список словарей, у которых в описании есть данная строка - `banking_transaction_data`
* Функция принимает список словарей с данными о банковских операциях и список категорий операций,
а возвращает словарь, в котором ключи - это названия категорий - `count_description`
## Инструкция по установке
1. Чтобы скачать репозиторий:
```commandline
git clone https://github.com/GostischevAndrey/homework.git
```
2. Установите зависимости
```commandline
poetry install
```
## Тестирование 
Проект протестирован Pytest

## Логирование
1. Файлы логов записываются в папку logs
2. Для модуля masks.py - masks.log
3. Для модуля utils.py - utils.log
4. Файлы логов перезаписываемые

Чтобы запустить тесты с оценкой покрытия выполните команду
```commandline
poetry run pytest --cov
```
Чтобы сгенерировать отчет о покрытии в HTML-формате, где src — пакет c модулями, которые тестируем. 
Отчет будет сгенерирован в папке htmlcov и храниться в файле с названием index.html
.
```commandline
pytest --cov=src --cov-report=html
```
## Команда проекта:
* Гостищев Андрей — Back-End developer
## Контакт для связи с командой разработки:
* pise4kan8@gmail.com
## Источники
Программа создана при поддержке онлайн-школы - SkyPro - skypro@skyeng.ru
