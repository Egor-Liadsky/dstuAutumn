import unittest
from server.database import requests as DBOperator

class MyTestCase(unittest.TestCase):
    def test_select_user_valid(self):
        print(DBOperator.DbOperator().select_user('egor@mail.ru', "+1111"))

    def test_select_user_invalid(self):
        print(DBOperator.DbOperator().select_user('sdfasdfasdfegor@mail.ru', "+sadfasdf1111"))


if __name__ == '__main__':
    unittest.main()
