![Static Badge](https://img.shields.io/badge/Python-%2350C878?style=for-the-badge&logo=python)
![Static Badge](https://img.shields.io/badge/PyQt-%2350C878?style=for-the-badge&logo=qt&logoColor=black)
![Static Badge](https://img.shields.io/badge/sqlalchemy-%2350C878?style=for-the-badge&logo=sqlalchemy&logoColor=black)
![Static Badge](https://img.shields.io/badge/alembic-%2350C878?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/pytest-%2350C878?style=for-the-badge&logo=pytest&logoColor=black)
![Static Badge](https://img.shields.io/badge/loguru-%2350C878?style=for-the-badge)


![Static Badge](https://img.shields.io/badge/postgresql-%2350C878?style=for-the-badge&logo=postgresql&logoColor=black)
![Static Badge](https://img.shields.io/badge/github%20actions-%2350C878?style=for-the-badge&logo=githubactions&logoColor=black)

<p align="center">
  <img src="https://github.com/Progger715/document-flow/assets/83240866/c271c1a4-140f-4bf1-9f9a-e4b4b7f3e5b2" alt="альтернативный текст">
</p>

# Оглавление

- [Описание проекта](#описание-проекта)
    - [Техническое описание проекта](#конфигурация)
- [Функциональность](#функциональность)
- [Инструкции по установке](#инструкции-по-установке)
    - [Конфигурация](#конфигурация)
- [Использование](#использование)
    - [Авторизация](#Авторизация)
    - [Роль пользователя](#Роль-пользователя)
    - [Роль администратора](#Роль-администратора)
    - [Роль супер-админа](#Роль-супер-админа)
- [Описание основных пакетов](#Описание-основных-пакетов)
- [Тестирование](#тестирование)

# Описание проекта

Проект представляет цифровой архив документов. Пользователи могут загружать в систему и выгружать документы,
исходя из своей матрицы доступа (подчинение отделов). В приложении есть 3 ключевые роли:

* Супер-админ

  Занимается настройкой всей системы, добавляет администраторов, настраивает матрицу доступа, создает отделы.
  Имеет доступ ко всем документам. Имеет доступ к функционалу администраторов. Супер-админ в системе только один.


* Админ

  Занимается настройкой пользователей и документов. Админов в системе может быть много.


* Пользователь

  Ключевая роль, загружает документы. Пользователи закрепляются за отделами и имеют доступ к документам, исходя из
  матрицы подчинения отделов. Пользователей в системе много.

Проект разработан под систему, в которой нет возможности хранить файлы отдельно от базы данных, поэтому файлы хранятся
напрямую в базе данных. Программа способна работать с файлами любых расширений.

## Техническое описание проекта

Проект реализован на языке Python 3.9

Графический интерфейс реализован при помощи PyQt5

За работу с базой данных отвечает библиотека SQLAlchemy

Для контроля миграций используется Alembic

Тесты реализованы с помощью фреймворка для тестирования Pytest

Проект реализован согласно концепции MVC. Модули разных уровней вынесены в отдельные пакеты

В проекте используется паттерн проектирования singleton (мета классы)

# Функциональность

Функционал различных ролей пользователей системы представлен в таблице ниже:

![Функционал](https://github.com/Progger715/document-flow/assets/83240866/2a882f86-da14-4161-8bc9-40278f9030e5)

# Инструкции по установке

1. Клонировать код на свое устройство

  ```bash
git clone https://github.com/Progger715/document-flow.git
  ```

2. Перейти в директорию с клонированным кодом

  ```bash
cd document-flow
  ```

3. Создать виртуальное окружение

  ```bash
python -m venv venv_df
  ```

4. Активировать виртуальное окружение

  ```bash
venv_df\Scripts\activate
  ```

5. Установить все зависимости

  ```bash
pip install -r requirements.txt
  ```

6. Создайте файл для переменных окружения

  ```bash
echo > src\config\.env
  ```

После чего заполните данный файл любым удобным для вас способом в соответствии с разделом [конфигурация](#конфигурация)

7. После заполнения файла .env, примените миграции и создайте все необходимые таблицы и зависимости:

  ```bash
  alembic upgrade head
  ```

8. После применения миграций, создайте супер-админа в системе и добавьте главный отдел
   (необходимо для дальнейшей работы приложения).
   Для этого выполните команду:

  ```bash
  python src/db/init_db.py
  ```

8. После этого все готово к работе. Запустите приложение командой:

  ```bash
  python run.py
  ```

Смотрите раздел [использование](#использование) для ознакомления с инструкцией использования приложения.

## Конфигурация

Расположение главного конфигурационного файла: *src/config/.env*. Данный файл отвечает за конфигурацию всей системы.
Содержимое файла *src/config/.env* следующее:

  ```dotenv
  LOGIN_DB=
  PASSWORD_DB=
  NAME_DB=
  HOST=
  PORT=
  HASH_FUNCTION=
  DIALECT_DB=
  DRIVER_DB=
  
  ```

Файл заполняется без кавычек. В конце обязательно должна быть пустая строка.

* LOGIN_DB - логин для базы данных
* PASSWORD_DB - пароль для базы данных
* NAME_DB - имя используемой базы данных
* HOST - хост на котором расположена используемая базы данных
* PORT - порт для подключения на хосте для базы данных
* HASH_FUNCTION - используемая хеш функция. Используется в связке с `hashlib.pbkdf2_hmac()`, для выбора возможных
  вариантов ознакомьтесь с [документацией](https://docs.python.org/3/library/hashlib.html)
* DIALECT_DB - используемая СУБД. Используется в связке с `sqlalchemy.create_engine()`, для выбора возможных вариантов
  ознакомьтесь с [документацией](https://docs.sqlalchemy.org/en/20/core/engines.html)
* DRIVER_DB - драйвер для СУБД. Используется в связке с `sqlalchemy.create_engine()`, для выбора возможных вариантов
  ознакомьтесь с [документацией](https://docs.sqlalchemy.org/en/20/core/engines.html)

# Использование

## Авторизация

После запуска приложения появляется окно авторизации.
<p align="center">
  <img src="https://github.com/Progger715/document-flow/assets/83240866/c6d9a6ee-aa5b-4c5e-9b68-b6baefa56e09" alt="Окно авторизации">
</p>
Необходимо выбрать роль: "пользователь" для пользователей системы, "админ" для супер-админов и администраторов системы.
Ввести логин и пароль.

Далее откроется одно из трех возможных окон:

1. Окно пользователя

<p align="center">
  <img src="https://github.com/Progger715/document-flow/assets/83240866/e6ce12ef-de7f-49b9-a001-9d04ffb7e316" alt="окно пользователя">
</p>

2. окно администратора

<p align="center">
  <img src="https://github.com/Progger715/document-flow/assets/83240866/81a8e064-b11c-4df6-b2ad-c5943e99ec26" alt="окно администратора">
</p>

3. окно супер-админа

<p align="center">
  <img src="https://github.com/Progger715/document-flow/assets/83240866/f20aa46f-a0d6-418c-9eae-04f47ae7549d" alt="окно супер-админа">
</p>

## Роль пользователя

Пользователю доступен следующий функционал:

* Просмотр документов, исходя из своей матрицы доступа
* Сортировать документы по любому интересующему столбцу. Для этого необходимо щелкнуть лкм по имени интересующего
  столбца
* Кнопка _"Главная"_ - вывод списка документов до применения поиска и периода (без обращения к бд)
* Кнопка _"Обновить"_ - обновление списка документов (обращение к бд)
* Кнопка _"Искать"_ - работает совместно с полем для поиска. Производит поиск документов в базе по поисковому слову.
  Поиск происходит по части слова, по всем полям таблицы, кроме дат
* Кнопка _"Период"_ - поиск по заданному периоду исходящий даты и/или даты загрузки
* Кнопка _"Добавить"_ - загрузить новый документ в систему

<p align="center">
  <img src="https://github.com/Progger715/document-flow/assets/83240866/871e9a0a-75d3-43d5-a304-758cd891e335" alt="окно загрузки документа">
</p>

* Кнопка _"Редактировать"_ - недоступна для пользователей
* Кнопка _"Удалить"_ - недоступна для пользователей
* Кнопка _"Выйти"_ - завершение сеанса пользователя, выход на окно авторизации
* Кнопка _"Скачать"_ - загрузка файла документа из системы на устройство

## Роль администратора

Администратору доступны следующие режимы работы:

1. Режим работы с документами

<p align="center">
  <img src="https://github.com/Progger715/document-flow/assets/83240866/81a8e064-b11c-4df6-b2ad-c5943e99ec26" alt="режим работы с документами">
</p>

В данном режиме администратор может делать все то же, что и пользователь, за исключением следующих возможностей:

* Администратору доступны все без исключения документы для просмотра
* Кнопка _"Добавить"_ - недоступна для администратора
* Кнопка _"Редактировать"_ - редактировать данные выбранного документа
* Кнопка _"Удалить"_ - удалить выбранный документ

2. Режим работы с пользователями

<p align="center">
  <img src="https://github.com/Progger715/document-flow/assets/83240866/21af2f09-58c7-4284-9f2c-158e024173f8" alt="режим работы с пользователями">
</p>

В данном режиме администратор может:

* Просматривать учетные записи пользователей
* Сортировать учетные записи пользователей по любому интересующему столбцу.
  Для этого необходимо щелкнуть лкм по имени интересующего столбца
* Кнопка _"Главная"_ - вывод списка учетных записей пользователей до применения поиска и периода (без обращения к бд)
* Кнопка _"Обновить"_ - обновление списка учетных записей пользователей (обращение к бд)
* Кнопка _"Искать"_ - работает совместно с полем для поиска. Производит поиск учетных записей пользователей в базе по
  поисковому слову. Поиск происходит по части слова, по всем полям таблицы, кроме дат
* Кнопка _"Период"_ - поиск по заданному периоду даты регистрации пользователя
* Кнопка _"Добавить"_ - создать новую учетную запись пользователя
* Кнопка _"Редактировать"_ - редактировать данные выбранной учетной записи пользователя
* Кнопка _"актив/деактив"_ - активировать или деактивировать выбранную учетную запись пользователя

## Роль супер-админа

Супер-админу доступны следующие режимы работы:

1. Режим работы с документами

В данном режиме супер-админ может делать все то же, что и администратор

2. Режим работы с пользователями

В данном режиме супер-админ может делать все то же, что и администратор

3. Режим работы с администраторами

<p align="center">
  <img src="https://github.com/Progger715/document-flow/assets/83240866/fb5199fc-0c1b-428c-a46f-2b3900a857bb" alt="режим работы с администраторами">
</p>

В данном режиме супер-админ может:

* Просматривать учетные записи администраторов
* Сортировать учетные записи администраторов по любому интересующему столбцу.
  Для этого необходимо щелкнуть лкм по имени интересующего столбца
* Кнопка _"Главная"_ - вывод списка учетных записей администраторов до применения поиска и периода (без обращения к бд)
* Кнопка _"Обновить"_ - обновление списка учетных записей администраторов (обращение к бд)
* Кнопка _"Искать"_ - работает совместно с полем для поиска. Производит поиск учетных записей администраторов в базе по
  поисковому слову. Поиск происходит по части слова, по всем полям таблицы, кроме дат
* Кнопка _"Период"_ - поиск по заданному периоду даты регистрации администратора
* Кнопка _"Добавить"_ - создать новую учетную запись администратора
* Кнопка _"Редактировать"_ - редактировать данные выбранной учетной записи администратора
* Кнопка _"актив/деактив"_ - активировать или деактивировать выбранную учетную запись администратора

4. Режим работы с матрицей доступа отделов

<p align="center">
  <img src="https://github.com/Progger715/document-flow/assets/83240866/5a0c2f54-fffb-499d-a040-c2ac4da464e4" alt="режим работы с матрицей доступа отделов">
</p>


В данном режиме супер-админ может:

* Просматривать существующую матрицу доступа отделов (все отделы и подчинение)
* Редактировать данные отдела
* Редактировать вложенность отделов (подчинение)
* Кнопка _"сохранить изменения"_ - сохраняет все примененные изменения и добавленные отделы. *Без нажатия данной кнопки
  внесенные изменения не будут применены к системе*
* Кнопка _"добавить элемент"_ - создать новый отдел
* Кнопка _"удалить элемент"_ - удалить выбранный отдел

# Описание основных пакетов

### 1. src/model

Данный пакет представляет собой уровень Model согласно MVC паттерну.

* Логика модели разнесена в отдельные файлы согласно ролям системы: супер-админ, админ, пользователь.
* _singleton_meta.py_ отвечает за реализацию singleton паттерна через метаклассы
* _handler_hierarchy.py_ вспомогательный модуль для работы с иерархией подчинения отделов

#### 1.1 src/model/utils

Пакет с утилитами для уровня модели.

А так же в данном пакете содержится пакет с кастомными исключениями приложения.

### 2. src/db

Данный пакет реализует функционал для работы с базой данных, а именно модели бд и методы согласно ролям пользователей
системы.

Работа с базой данных осуществляется через SQLAlchemy.

В корне данного пакета находится окно авторизации, а так же главные окна для режимов работы с: документами,
пользователями, администраторами, матрицей доступа

### 3. src/view

Данный пакет представляет собой уровень View согласно MVC паттерну. Все представление разработано на PyQt5.

В корне данного пакета находится окно авторизации, а так же главные окна для режимов работы с: документами,
пользователями, администраторами, матрицей доступа

#### 3.1 src/view/dialog_window

Диалоговые окна приложения

#### 3.2 src/view/widget

Кастомные виджеты приложения

### 4. src/controller

Данный пакет представляет собой уровень Controller согласно MVC паттерну.

* _controller_main_window.py_ непосредственно контроллер, перенаправляющий все запросы с уровня View на уровень Model
* _logger_controller.py_ модуль для логирования действий пользователей в системе. Логи сохраняются в директорию _logs_.

### 5. src/tests

Данный пакет отвечает за тесты приложения. Все тесты разработаны на Pytest.
В корне данного пакета находится главный конфигурационный файл тестов.

#### 5.1 src/tests/func_tests

Пакет функциональных тестов проекта

#### 5.2 src/tests/unit_tests

Пакет Юнит тестов проекта

# Тестирование

Тесты расположены в директории [src/tests](#5.-src/tests).

Для запуска всех тестов выполнить:

```bash
pytest -v .\src\tests\  
```

Для запуска отдельно юнит тестов выполнить:

```bash
pytest -v .\src\tests\unit_tests\  
```

Для запуска отдельно функциональных тестов выполнить:

```bash
pytest -v .\src\tests\func_tests\  
```

Для запуска тестов с другим форматом вывода информации или режимом тестирования обратитесь к
[документации pytest](https://docs.pytest.org/en/7.1.x/contents.html)