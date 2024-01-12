#!/usr/bin/python3
"""Unit test for Base Model"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class for unit test -> BaseModel"""

    def SetUp(self):
        model_for_test = BaseModel()

    def TearDown(self):
        pass

    def test_str(self):
        self.assertequal(model_for_test.__str__(),
                          f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

if __name__ == "__main__":
    unittest.main()
