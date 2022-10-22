import unittest
from server.database import handler


class MyTestCase(unittest.TestCase):
    def test_connect(self):
        handler.Db()

    def test_check_user_valid(self):
        handler.Db()._select_with_email("egor@mail.ru")

    def test_check_user_invalid(self):
        handler.Db()._select_with_email("sdfasdfasdfasdf")

    def test_new_user(self):
        handler.Db().new_user('egor@mail.ru','rand', 'egor lyad', "+1111")


if __name__ == '__main__':
    unittest.main()
