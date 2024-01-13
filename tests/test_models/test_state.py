#!/usr/bin/python3
"""Test the State class"""


import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test the State class"""

    def setUp(self):
        """Set up the test case"""
        self.state = State()

    def test_instantiation(self):
        """Test that object is correctly created"""
        self.assertIsInstance(self.state, State)

    def test_name(self):
        """Test that name attribute is an empty string"""
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        """Test that State class inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == '__main__':
    unittest.main()
