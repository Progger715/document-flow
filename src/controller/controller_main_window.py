import src.model.for_data_base.db_helper as db_helper_for_documents_and_users

from src.model import handler_hierarchy
from src.model.user import User
from src.model.administrator import Administrator
from src.model.super_admin import SuperAdmin

from src.model.custom_exceptions import ClientPasswordError, ClientActiveError, ClientNotFoundError, FileNotWrittenError
from typing import Tuple, Optional

client = SuperAdmin  # Client("admin").client


def authenticate(login: str, password: str, role: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Performs user authentication with error handling
    :param login:
    :param password:
    :param role:
    :return: role: str or None, error:str or None
    """
    try:
        user = __check_login(login, password, role)
        return user, None  # Возвращаем объект пользователя и None в качестве ошибки
    except (ClientActiveError, ClientNotFoundError, ClientPasswordError) as ex:
        return None, str(ex)
    except Exception as ex:
        # log
        return None, f"Неизвестная ошибка, обратитесь к разработчикам. \nКод ошибки: 001"


def __check_login(login: str, password: str, role: str):
    """

    :param login:
    :param password:
    :param role: 'admin' or 'user'
    :return: 'admin' or 'user' or 'superAdmin' or message about error
    """
    if role not in ("admin", "user"):
        raise ValueError("Значение role ожидается 'admin' или 'user'")
    global client  # , role_client

    if role == 'admin':
        client = Administrator()
        result = client.check_password(login, password)  # superAdmin or Admin
        # role_client = result
        if result == 'superAdmin':
            client = SuperAdmin()
        return result

    elif role == 'user':
        # role_client = role
        client = User()
        result = client.check_password(login, password)
        return result


def save_hierarchy(list_hierarchy: list):
    # log
    handler_hierarchy.save_hierarchy(list_hierarchy)


def get_hierarchy():
    hierarchy = handler_hierarchy.Hierarchy()
    return hierarchy.get_data_about_departments()


def add_user_in_database(last_name: str, name: str, patronymic: str, login: str, password: str, id_department: int):
    # log
    client.add_user(last_name, name, patronymic, login, password, id_department)


def add_document_in_database(path_to_document: str, name_document: str, inner_number: str, output_number: str,
                             output_date, type_document: str):
    # log
    client.add_document(path_to_document, name_document, inner_number, output_number, output_date, type_document)


def get_data_about_documents():
    # log
    return client.get_data_about_documents()


def download_document(id_document: int, path_to_save: str):
    # log
    try:
        client.download_document(id_document, path_to_save)
        print("Документ сохранен")
    except FileNotFoundError:
        return "Путь для сохранения файла недопустим"
    except FileNotWrittenError:
        return str(FileNotWrittenError)
    except Exception as ex:
        return "Неизвестная ошибка, обратитесь в отдел разработки. \nКод ошибки 201"


def delete_document(id_document: int):
    # log
    # db_helper_for_documents_and_users.delete_file(name_document, inner_number, output_number)
    client.delete_document(id_document)


def edit_document(id_document: int, name_document: str, inner_number: str, output_number: str,
                  output_date, type_document: str):
    # log
    client.edit_document(id_document, name_document, inner_number, output_number, output_date, type_document)


def get_data_about_users():
    # log
    return client.get_data_about_users()


def change_activation_status(id_user: int):
    client.change_activation_status(id_user)


def edit_user_data(last_name: str, name: str, patronymic: str, login: str, password: str, id_user: int,
                   id_department: int):
    # log
    client.edit_user_data(last_name, name, patronymic, login, password, id_department=id_department, id_user=id_user)


def add_admin_in_database(last_name: str, name: str, patronymic: str, login: str, password: str):
    # log
    client.add_admin(last_name, name, patronymic, login, password)


def get_data_about_admins():
    # log
    data = client.get_data_about_admins()
    return data


def change_activation_status_admin(id_admin: int):
    # log
    client.change_activation_status_admin(id_admin)


def edit_admin_data(id_admin: int, new_last_name: str, new_name: str, new_patronymic: str, new_login: str,
                    new_password: str, flag_edit_login: bool):
    client.edit_admin_data(id_admin, new_last_name, new_name, new_patronymic, new_login, new_password, flag_edit_login)


def add_department(name_department: str, number_department: int):
    return handler_hierarchy.add_department_in_db(name_department, number_department)


def add_one_hierarchy(id_department: int, parent_id: int):
    handler_hierarchy.add_one_hierarchy(id_department, parent_id)


def delete_departments(id_departments_for_delete: list):
    handler_hierarchy.delete_departments(id_departments_for_delete)


#
# def delete_department(id_department: int):
#     # log
#     handler_hierarchy.delete_department_in_db(id_department)


def update_data_departments(list_departments: list):
    # log
    handler_hierarchy.update_data_departments(list_departments)


def change_people_departments(list_replacement_departments: list):
    # log
    handler_hierarchy.change_people_departments(list_replacement_departments)


def change_password(password: str):
    # log
    return client.change_password(password)


def check_needs_password_change():
    # log
    # client = User()
    return client.check_needs_password_change()


def get_login():
    # log
    return client.get_login()


def get_role():
    return client.get_role()


def get_full_name():
    return client.get_full_name()


def get_number_department():
    return client.get_number_department()


def check_password_strength(password: str):
    return client.check_password_strength(password)


def search_documents(search_string: str):
    # log
    return client.search_string_in_documents(search_string)


def apply_period_searching_documents(flag_date_output: bool, flag_date_download: bool,
                                     start_date_output: str = None, end_date_output: str = None,
                                     start_date_download: str = None, end_date_download: str = None):
    # log
    return client.apply_period_searching_documents(flag_date_output, flag_date_download,
                                                   start_date_output=start_date_output, end_date_output=end_date_output,
                                                   start_date_download=start_date_download,
                                                   end_date_download=end_date_download)


def search_users(search_string: str):
    # log
    return client.search_string_in_users(search_string)


def search_admins(search_string: str):
    # log
    return client.search_string_in_admins(search_string)


def apply_period_registration_admins(start_date_download: str, end_date_download: str):
    return client.apply_period_registration_admins(start_date_download, end_date_download)
    # return []


def apply_period_searching_registration_users(start_date_download: str, end_date_download: str):
    return client.apply_period_registration_users(start_date_download, end_date_download)
    # return []
