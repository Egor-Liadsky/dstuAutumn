import psycopg2
from server.settings import database as setting

class Db:
    def __init__(self):
        self.connection = psycopg2.connect(user=setting.USER,
                                      password=setting.PASSWORD,
                                      host=setting.HOST,
                                      port=setting.PORT)

    def select_password(self, user: str) -> str:
        pass

    def new_user(self, user: str, secret_key: str, public_key: str, public_name: str) -> str:
        pass

