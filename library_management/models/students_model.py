from util.db import DBConnection
from util.queries import INSERT_STUDENT,get_students
from flask_login import UserMixin

class StudentModel(UserMixin):

    def __init__(self, id,name,email,reg_no,active=True,created_on= None):
        self.id = id
        self.name = name
        self.email = email
        self.reg_no = reg_no
        self.active=active
        self.created_on = created_on


    @staticmethod
    def create_Student(name,email,reg_no,current_user_id):
        try:
            conn = DBConnection.get_conn()
            curr = conn.cursor()
            curr.execute(INSERT_STUDENT, (name,email,reg_no,current_user_id))
            conn.commit()
            curr.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Exception Handled in student POST block- {e}")
            return False

    @classmethod
    def get_student(cls):
        try:
            conn = DBConnection.get_conn()
            curr = conn.cursor()
            curr.execute(get_students)
            data = curr.fetchall()
            curr.close()
            conn.close()
            students = []
            for student in data:
                print(student)
                b = StudentModel(student[0], student[1], student[2], student[3])
                students.append(b)
            return students
        except Exception as e:
            print(f"Exception in create_book {e}")
            return False
