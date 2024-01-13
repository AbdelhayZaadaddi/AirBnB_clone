#!usr/bin/python3
"""Test the Review class"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test the Review class"""

    def setUp(self):
        """Set up the test case"""
        self.review = Review()

    def test_instantiation(self):
        """Test that object is correctly created"""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """Test that attributes have the correct default values"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        """Test that Review class inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == '__main__':
    unittest.main()
