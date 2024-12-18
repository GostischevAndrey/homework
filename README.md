# Banking operations widget
## Описание проекта
Программа создана для фильтрации, генерации и сортировки банковских карт и счетов, по дате и оплате.
## Project dependencies:
* The program uses the version Python 3.13
* flake8 = "^7.1.1"
* black = "^24.10.0"
* isort = "^5.13.2"
* mypy = "^1.13.0"
## Функции, которые мы будем использовать:
* Функция скрывающая номер карты и счета - `mask_account_card`
* Функция сортировки по дате - `sort_by_date`
* Функция фильтрации в операциях по счетам - `filter_by_state`
* Функция выдающая список транзакций в определенной валюте -`filter_by_currency`
* Функция выдающая описание операций - `transaction_descriptions`
* Функция генерирующая номера карт - `card_number_generator`
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
