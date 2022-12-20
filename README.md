# Проект Employee_record

## Описание

Employee_record это сервис для записи работник.

Пользователи могут записать работника и получить эксель файл с данными последних пяти работников

## Технологии
- Python 3.7.9
- pyTelegramBotAPI==4.8.0
- SQLAlchemy==1.4.45
- alembic==1.9.0

## Установка проекта локально

* Склонировать репозиторий на локальную машину:
```bash
git clone https://github.com/niktere12321/Employee_record.git
```
```bash
cd Employee_record
```

- Создать и заполнить по образцу .env-файл
```
TOKEN=<ваш токен>
```

* Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

* Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

* Выполните миграции:
```bash
alembic upgrade head
```

---
## Об авторе

Терехов Никита Алексеевич