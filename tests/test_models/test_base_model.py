#!/usr/bin/python3
"""Unit tests for the BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class"""

    def setUp(self):
        """Set up testing environment"""
        self.model = BaseModel()

    def test_init_no_args(self):
        """Test initialization with no arguments"""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_init_with_args(self):
        """Test initialization with arguments"""
        model = BaseModel(
            id="1234",
            created_at="2022-01-01T12:00:00.000000",
            updated_at="2022-01-01T12:00:00.000000"
        )
        self.assertEqual(model.id, "1234")
        self.assertEqual(model.created_at, datetime(2022, 1, 1, 12))
        self.assertEqual(model.updated_at, datetime(2022, 1, 1, 12))

    def test_str(self):
        """Test string representation of the model"""
        model_str = str(self.model)
        self.assertTrue("[BaseModel] ({})".format(self.model.id) in model_str)
        self.assertTrue("'id': '{}'".format(self.model.id) in model_str)

    def test_to_dict(self):
        """Test conversion of the model to a dictionary"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        ct = model_dict["created_at"]
        md = model_dict["updated_at"]
        self.assertEqual(ct, self.model.created_at.isoformat())
        self.assertEqual(md, self.model.updated_at.isoformat())

    def test_save(self):
        """Test saving the model"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_init_with_unexpected_args(self):
        """Test initialization with unexpected arguments"""
        model = BaseModel(unexpected_arg="unexpected")
        self.assertFalse(hasattr(model, "unexpected_arg"))

    def test_str_with_additional_attributes(self):
        """Test string representation with additional attributes"""
        self.model.name = "Test"
        model_str = str(self.model)
        self.assertTrue("'name': 'Test'" in model_str)

    def test_to_dict_with_additional_attributes(self):
        """Test conversion to dictionary with additional attributes"""
        self.model.name = "Test"
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["name"], "Test")

    def test_save_updates_updated_at(self):
        """Test that save updates the updated_at attribute"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_save_does_not_update_created_at(self):
        """Test that save does not update the created_at attribute"""
        old_created_at = self.model.created_at
        self.model.save()
        self.assertEqual(self.model.created_at, old_created_at)


if __name__ == '__main__':
    unittest.main()
