#!/usr/bin/python3
"""Test the Amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def setUp(self):
        """Set up the test case"""
        self.amenity = Amenity()

    def test_instantiation(self):
        """Test that object is correctly created"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_name(self):
        """Test that name attribute is an empty string"""
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """Test that Amenity class inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == '__main__':
    unittest.main()
