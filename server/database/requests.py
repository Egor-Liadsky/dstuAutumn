import handler
class DbOperator:
    def new_user(self, user: str, secret_key: str, public_key: str, public_name: str):
        handler.Db().new_user(user, secret_key, public_key, public_name)

