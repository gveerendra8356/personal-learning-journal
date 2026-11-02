import unittest
from login import hash_password, login


class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        salt = b"test-only-salt-01"
        cls.users = {"learner": (salt, hash_password("example-password", salt))}

    def test_valid_credentials(self):
        self.assertTrue(login("learner", "example-password", self.users))

    def test_wrong_password(self):
        self.assertFalse(login("learner", "incorrect", self.users))

    def test_unknown_user(self):
        self.assertFalse(login("unknown", "example-password", self.users))

    def test_empty_or_invalid_input(self):
        for name, password in [("", "x"), ("learner", ""), (None, "x")]:
            with self.subTest(name=name, password=password):
                self.assertFalse(login(name, password, self.users))
