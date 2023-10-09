
from flask_login import UserMixin

from util.db import DBConnection
from util.queries import GET_USER_BY_ID, GET_USER_BY_EMAIL, INSERT_EMPLOYEE


class UserModel(UserMixin):

    def __init__(self, user_id, email, name, password, is_active=True):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.active = is_active

    @classmethod
    def get_user_by_id(cls, user_id):
        if not user_id:
            raise ValueError(f"Invalid User ID {user_id}")
        return cls.get_user_data(GET_USER_BY_ID, (user_id, ))

    @classmethod
    def get_user_by_email(cls, email_id):
        if not email_id:
            raise ValueError(f"Invalid User ID {email_id}")
        return cls.get_user_data(GET_USER_BY_EMAIL, (email_id, ))

    @classmethod
    def get_user_data(cls, query, params):
        conn = DBConnection.get_conn()
        curr = conn.cursor()
        curr.execute(query, params)
        result = curr.fetchone()
        curr.close()
        conn.close()
        if result:
            return UserModel(result[0], result[2], result[1], result[3], result[4])
        else:
            return None

    @staticmethod
    def register_employee(name, email, password):
        conn = DBConnection.get_conn()
        curr = conn.cursor()
        curr.execute(INSERT_EMPLOYEE, (name, email, password))
        conn.commit()
        curr.close()
        conn.close()


    @staticmethod
    def authenticate_user(email, password):
        user = UserModel.get_user_by_email(email)
        if user:
            print(password)
            print(user.password)
            if password == user.password:
                return {"success": True, "message": "Authenticated Successfully", "user": user}
            else:
                return {"success": False, "message": "Invalid Password"}
        else:
            return {"success": False, "message": "Invalid Email"}