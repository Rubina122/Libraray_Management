
from util.db import DBConnection
from util.queries import INSERT_BOOK, GET_BOOKS, GET_BOOK_BY_ID

class BookModel:

    def __init__(self, id, title, author, total_copies, available_copies=None, created_by=None, bought_on=None):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies
        self.created_by = created_by
        self.bought_on = bought_on

    @staticmethod
    def create_book(title, author, total_copies, current_user_id):
        try:
            conn = DBConnection.get_conn()
            curr = conn.cursor()
            curr.execute(INSERT_BOOK, (title, author, total_copies, total_copies, current_user_id))
            conn.commit()
            curr.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Exception in create_book {e}")
            return False


    @classmethod
    def get_books(cls):
        try:
            conn = DBConnection.get_conn()
            curr = conn.cursor()
            curr.execute(GET_BOOKS)
            data = curr.fetchall()
            curr.close()
            conn.close()
            books = []
            for book in data:

                b = BookModel(book[0], book[1], book[2], book[3], book[4], book[6], book[5])
                books.append(b)
            return books
        except Exception as e:
            print(f"Exception in create_book {e}")
            return False


    @classmethod
    def get_book_by_id(cls, id):
        conn = DBConnection.get_conn()
        curr = conn.cursor()
        curr.execute(GET_BOOK_BY_ID, (id, ))
        book = curr.fetchone()
        b = None
        if book:
            b = BookModel(id, book[0], book[1], book[2])
        curr.close()
        conn.close()
        return b