#!/usr/bin/python3
"""Test the City class"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test the City class"""

    def setUp(self):
        """Set up the test case"""
        self.city = City()

    def test_instantiation(self):
        """Test that object is correctly created"""
        self.assertIsInstance(self.city, City)

    def test_state_id(self):
        """Test that state_id attribute is an empty string"""
        self.assertEqual(self.city.state_id, "")

    def test_name(self):
        """Test that name attribute is an empty string"""
        self.assertEqual(self.city.name, "")

    def test_inheritance(self):
        """Test that City class inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == '__main__':
    unittest.main()
