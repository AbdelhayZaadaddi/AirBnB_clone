#!/usr/bin/python3
"""Unit test for Base Model"""

import unittest
import os
from models.base_model import BaseModel

print(os.getcwd())
class TestBaseModel(unittest.TestCase):
    """class for unit test -> BaseModel"""

    def setUp(self):
        print("setup") 
        self.model = BaseModel()

    def tearDown(self):
        print("tear down")

    def test_str(self):
        #model = BaseModel()
        self.assertEqual(8,4+4)
        self.assertEqual(self.model.__str__(),
                         f"[{self.model.__class__.__name__}] ({self.model.id}) {self.model.__dict__}")

if __name__ == "__main__":
    unittest.main()
