import typing

from server.database import handler
class DbOperator:
    def select_user(self, email: str, number: str) -> bool:
        handlerDb = handler.Db()
        select_email = handlerDb._select_with_email(email)
        select_number = handlerDb._select_with_number(number)
        if isinstance(select_email, tuple) and isinstance(select_number, tuple):
            return select_number[-1]
        return False
    def select_user_info(self, id: int) -> typing.Tuple[str]:
        return handler.Db()._select_user_info(id)

