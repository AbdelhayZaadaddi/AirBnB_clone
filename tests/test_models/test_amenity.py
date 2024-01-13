#!/usr/bin/python3
"""Unit test for Amenity"""

import unittest
import os
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """class for unit test -> Amenity"""

    def setUp(self):
        """Set Up the two models"""
        self.model = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """Tear down function"""
        pass


if __name__ == "__main__":
    unittest.main()
