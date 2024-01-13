#!/usr/bin/python3
"""Unit test for Base Model"""

import unittest
import os
from models.base_model import BaseModel

#print(os.getcwd())
class TestBaseModel(unittest.TestCase):
    """class for unit test -> BaseModel"""

    def setUp(self):
        #print("setup") 
        """Set Up the two models"""
        self.model = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """Tear down function"""
        pass #print("tear down")

    def test_str(self):
        """Test the str method"""
        #model = BaseModel()
        self.assertEqual(8,4+4)
        self.assertEqual(self.model.__str__(),
                         f"[{self.model.__class__.__name__}] ({self.model.id}) {self.model.__dict__}")

    def test_uuid(self):
         """Test the id uniqueness"""
         self.assertNotEqual(self.model.id, self.model2.id)

    def test_save(self):
        """Test save method"""
        self.model.save()
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

if __name__ == "__main__":
    unittest.main()
