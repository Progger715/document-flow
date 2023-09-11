"""file with database access methods for admin role"""
import pydantic
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.db.database_setup import get_engine
from src.db.models.admins import Admins
from src.db.models.users import Users


class AdminDB:
    # _________________________________ADD______________________________________________________
    @staticmethod
    @pydantic.validate_arguments
    def add_user(last_name: str, name: str, patronymic: str, login: str, password: bytes, salt: bytes,
                 id_department: int, id_creator: int) -> int:
        with Session(get_engine()) as session:
            with session.begin():
                new_user = Users(name=name, last_name=last_name, patronymic=patronymic, login=login,
                                 password=password, salt=salt, creator_id=id_creator, id_department=id_department)

                session.add(new_user)
                session.commit()
            return new_user.id

    # _________________________________GET_______________________________________________________
    @staticmethod
    @pydantic.validate_arguments
    def check_password(login: str) -> {}:
        with Session(get_engine()) as session:
            with session.begin():
                result = session.execute(
                    select(
                        Admins.id,
                        Admins.last_name,
                        Admins.name,
                        Admins.patronymic,
                        Admins.active,
                        Admins.password,
                        Admins.salt,
                        Admins.super_admin_flag,
                        Admins.date_last_changes_password
                    ).where(Admins.login == login))
            result = result.mappings().fetchone()
            return result

    @staticmethod
    @pydantic.validate_arguments
    def get_all_users():
        with Session(get_engine()) as session:
            with session.begin():
                result = session.execute(select(Users.__table__))
                users = result.mappings().fetchall()
                return users

    @staticmethod
    @pydantic.validate_arguments
    def get_one_user(id_user: int):
        with Session(get_engine()) as session:
            with session.begin():
                result = session.execute(
                    select(Users.__table__).where(Users.__table__.c.id == id_user))
                user = result.mappings().fetchone()
                return user

    # ________________________________UPDATE_____________________________________________________
    @staticmethod
    @pydantic.validate_arguments
    def update_user(id_user: int, **kwargs):
        # Найти запись по user_id
        with Session(get_engine()) as session:
            with session.begin():
                user = session.query(Users).filter_by(id=id_user).first()
                if user:
                    # Обновляем только переданные атрибуты
                    for key, value in kwargs.items():
                        if value is not None and value != "":
                            setattr(user, key, value)
                    session.commit()
                else:
                    raise ValueError(f"Пользователь с id {id_user} не найден.")
