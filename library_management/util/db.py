import psycopg2


class DBConnection:

    DB_NAME = "library_management"
    DB_USER = "postgres"
    DB_PASSWORD = "rahila"
    DB_HOST = "localhost"
    DB_PORT = "5432"

    @classmethod
    def get_conn(cls):
        return psycopg2.connect(dbname=cls.DB_NAME, user=cls.DB_USER, password=cls.DB_PASSWORD)

