#!/usr/bin/python3
"""Unit test for Base Model"""

import unittest
import os
#from models.base_model import BaseModel

print(os.getcwd())
class TestBaseModel(unittest.TestCase):
    """class for unit test -> BaseModel"""

    def SetUp(self):
         pass #model_for_test = BaseModel()

    def TearDown(self):
        pass

    def test_str(self):
        self.assertEqual(8,4+4)

        #self.assertequal(model_for_test.__str__(),
                          #f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

if __name__ == "__main__":
    unittest.main()
