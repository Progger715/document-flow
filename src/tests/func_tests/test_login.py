import pytest
import src.controller.controller_main_window as controller
from src.model.custom_exceptions.client_custom_exceptions import ClientNotFoundError, ClientPasswordError


@pytest.mark.parametrize("login, password, role, expected_exception",
                         [
                             ("ivanadmin", "password1", "admin", None),  # успешный вход
                             ("ivanadmin", "password1", "user", ClientNotFoundError),  # не найден в базе админ
                             ("ivan", "password1", "admin", ClientNotFoundError),  # не найден в базе админ
                             ("petradmin", "password", "admin", ClientPasswordError),  # неверный пароль
                         ])
def test_login(fill_db_admins, login, password, role, expected_exception):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            controller.__check_login(login, password, role)
        return
    assert role == controller.__check_login(login, password, role)
