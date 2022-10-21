import unittest
from server.database import handler


class MyTestCase(unittest.TestCase):
    def test_connect(self):
        handler.Db()

    def test_check_user_valid(self):
        handler.Db()._select_with_email("egor@mail.ru")

    def test_check_user_invalid(self):
        handler.Db()._select_with_email("sdfasdfasdfasdf")

if __name__ == '__main__':
    unittest.main()
