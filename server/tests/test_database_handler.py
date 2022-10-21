import unittest
from server.database import handler


class MyTestCase(unittest.TestCase):
    def test_connect(self):
        handler.Db()

    def test_check_user_valid(self):
        handler.Db().select_password('egor')

if __name__ == '__main__':
    unittest.main()
