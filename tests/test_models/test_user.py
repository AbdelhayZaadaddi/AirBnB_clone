#!/usr/bin/python3
"""Unit tests for the User class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up test environment"""
        self.user = User()

    def test_init(self):
        """Test initialization of User instance"""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test attributes of User class"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_update_attributes(self):
        """Test updating User attributes"""
        self.user.email = "test@example.com"
        self.user.password = "password"
        self.user.first_name = "First"
        self.user.last_name = "Last"
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "First")
        self.assertEqual(self.user.last_name, "Last")

    def test_inheritance(self):
        """Test User inheritance from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_type_attributes(self):
        """Test type of User attributes"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_empty_string_attributes(self):
        """Test User attributes are empty strings by default"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict_method(self):
        """Test conversion of User instance to dictionary"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(type(user_dict["created_at"]), str)
        self.assertEqual(type(user_dict["updated_at"]), str)
        self.assertEqual(user_dict["email"], self.user.email)
        self.assertEqual(user_dict["password"], self.user.password)
        self.assertEqual(user_dict["first_name"], self.user.first_name)
        self.assertEqual(user_dict["last_name"], self.user.last_name)

    def test_str_method(self):
        """Test string representation of User instance"""
        user_str = str(self.user)
        u = self.user.id
        ud = self.user.__dict__
        self.assertEqual(user_str, "[User] ({}) {}".format(u, ud))


if __name__ == '__main__':
    unittest.main()
