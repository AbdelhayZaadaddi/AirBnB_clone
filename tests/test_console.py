#!/usr/bin/python3
"""Unit test for Console"""

import unittest
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """Unit Test for Console"""


    def setUp(self):
        """Set Up the two models"""
        self.model = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """Tear down function"""
        pass


if __name__ == "__main__":
    unittest.main()
