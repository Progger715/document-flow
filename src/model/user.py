import os
from datetime import datetime
import datetime

from src.model.utils import tools
from src.config.types_role import Role
from src.model.utils.custom_exceptions import ClientPasswordError, ClientActiveError, ClientNotFoundError, \
    FileNotWrittenError

from src.db.methods.user_db_methods import UserDB
from src.model.singleton_meta import SingletonMeta


class User(metaclass=SingletonMeta):
    role = Role.USER

    def __init__(self):
        self.LVL_ACCESS = 2
        self.CURRENT_ID: int = None
        self.CURRENT_NAME: str = None
        self.CURRENT_LAST_NAME: str = None
        self.CURRENT_PATRONYMIC: str = None
        self.CURRENT_LOGIN: str = None
        self.CURRENT_ID_DEPARTMENT: int = None
        self.CURRENT_NUMBER_DEPARTMENT: int = None
        self.DATE_LAST_CHANGES_PASSWORD = None

    def get_role(self):
        return self.role.name

    def get_id(self):
        return self.CURRENT_ID

    def get_lvl_access(self):
        return self.LVL_ACCESS

    def get_login(self):
        return self.CURRENT_LOGIN

    def get_full_name(self):
        return f"{self.CURRENT_LAST_NAME} {self.CURRENT_NAME} {self.CURRENT_PATRONYMIC}"

    def get_number_department(self):
        return self.CURRENT_NUMBER_DEPARTMENT

    def set_self_data(self, data_user: {}, login_user: str):
        self.CURRENT_LOGIN = login_user
        self.CURRENT_ID = data_user['id']
        self.CURRENT_NAME = data_user['name']
        self.CURRENT_PATRONYMIC = data_user['patronymic']
        self.CURRENT_LAST_NAME = data_user['last_name']
        self.DATE_LAST_CHANGES_PASSWORD = data_user['date_last_changes_password']
        self.CURRENT_ID_DEPARTMENT = data_user['id_department']
        self.CURRENT_NUMBER_DEPARTMENT = data_user['number_department']

    def check_password(self, login: str, password: str, setting_received_data=True):
        """
        checks user authentication

        :param setting_received_data: default True. install the received data to the user?
        :param login: user login
        :param password: user password
        :return: True if login success, else False
        """
        data_user: {} = UserDB.check_password(login)

        if data_user is None:
            raise ClientNotFoundError(f"Пользователь с логином '{login}' не найден в базе!\n"
                                      "Проверьте логин и выбранную роль пользователя")

        if not data_user['active']:
            raise ClientActiveError(f"Учетная запись пользователя '{login}' с указанными данными деактивирована.\n"
                                    "Для активации учетной записи обратитесь к администратору.")

        password = tools.create_hash_password(password, data_user['salt'])

        if password != bytes(data_user['password']):
            raise ClientPasswordError(f"Для пользователя '{login}' указан неправильный пароль")

        if setting_received_data:
            self.set_self_data(data_user=data_user, login_user=login)
        return Role.USER

    def change_password(self, password: str):
        try:
            if self.check_password(self.CURRENT_LOGIN, password, setting_received_data=False) == "user":
                return False  # старый и новый пароли сходятся
        except Exception:
            pass
        salt = os.urandom(16)
        password = tools.create_hash_password(password, salt)
        UserDB.changes_password(self.CURRENT_ID, password, salt, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
        return True

    def check_needs_password_change(self):
        """

        :return: True if needs change password, else False
        """
        if self.DATE_LAST_CHANGES_PASSWORD is None:
            return True
        delta_date = datetime.datetime.now() - self.DATE_LAST_CHANGES_PASSWORD
        if delta_date.days > 180:
            return True
        else:
            return False  # пароль не надо менять

    def add_document(self, path_to_document: str, name_document: str, inner_number: str, output_number: str,
                     output_date: str, type_document: str, note: str):

        file = open(path_to_document, 'rb')
        output_date = datetime.datetime.strptime(output_date, "%d.%m.%Y")
        UserDB.add_document(self.CURRENT_ID, file.read(), name_document, inner_number, output_number, output_date,
                            type_document, note)

    def get_data_about_documents(self):
        return UserDB.get_data_about_documents(self.CURRENT_ID_DEPARTMENT)

    def search_string_in_documents(self, search_string: str):
        return UserDB.find_document_word(self.CURRENT_ID_DEPARTMENT, search_string)

    def apply_period_searching_documents(self, flag_date_output: bool, flag_date_download: bool,
                                         start_date_output: str = None, end_date_output: str = None,
                                         start_date_download: str = None, end_date_download: str = None):
        start_date_output = datetime.datetime.strptime(start_date_output, "%d.%m.%Y")
        end_date_output = datetime.datetime.strptime(end_date_output, "%d.%m.%Y")
        start_date_download = datetime.datetime.strptime(start_date_download, "%d.%m.%Y")
        end_date_download = datetime.datetime.strptime(end_date_download, "%d.%m.%Y")
        return UserDB.find_document_period(self.CURRENT_ID_DEPARTMENT,
                                           flag_date_output=flag_date_output, flag_date_download=flag_date_download,
                                           start_output_date=start_date_output, end_output_date=end_date_output,
                                           start_create_date=start_date_download, end_create_date=end_date_download)

    @staticmethod
    def download_document(id_document: int, path_to_save: str):
        data_file: {} = UserDB.get_file(id_document)

        if data_file is None:
            raise FileNotWrittenError("Файл с указанным ID не найден в базе данных.")

        with open(path_to_save, 'wb') as file:
            file.write(bytes(data_file['file']))

    def check_password_strength(self, password: str):
        """
        Function for check security password.
        If password was security function return True, else return password vulnerability report.

        :param password: str
        :return: True, if the password is secure, else message (str) password vulnerability
        """

        # Проверяем длину пароля
        if len(password) < 12:
            return "Пароль должен содержать больше 12 символов"

        # Проверяем наличие хотя бы одной цифры
        if not any(char.isdigit() for char in password):
            return "Пароль должен содержать хотя бы одну цифру"

        # Проверяем наличие хотя бы одной буквы в верхнем регистре
        if not any(char.isupper() for char in password):
            return "Пароль должен содержать хотя бы одну заглавнуюю букву"

        # Проверяем наличие хотя бы одной буквы в нижнем регистре
        if not any(char.islower() for char in password):
            return "Пароль должен содержать хотя бы одну прописную букву"

        # Проверяем наличие хотя бы одного специального символа
        special_chars = """!@#$%^&*()_+-={}|[]\:;"'<>?,./"""
        if not any(char in special_chars for char in password):
            return f"Пароль должен содержать хотя бы один специальный символ ({special_chars})"

        # Проверяем на сходство с логином
        if password == self.CURRENT_LOGIN:
            return "Пароль не должен сходится с логином"

        # Если все проверки пройдены, то пароль сильный
        return True
