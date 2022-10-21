import psycopg2
import settings

class Db:
    def __init__(self):
        connection = psycopg2.connect(settings.database.USER,
                                      # пароль, который указали при установке PostgreSQL
                                      settings.database.PASSWORD,
                                      host="127.0.0.1",
                                      port="5432")
        pass

    def select_password(self, user: str) -> str:
        pass

    def set_secret_key(self, user: str, secret_key: str) -> str:
        pass

