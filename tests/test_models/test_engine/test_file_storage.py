#!/usr/bin/python3
"""Unit tests for the FileStorage class"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up testing environment"""
        self.storage = FileStorage()
        self.model = BaseModel()

    def test_all(self):
        """Test all method of FileStorage"""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """Test new method of FileStorage"""
        self.storage.new(self.model)
        key = "{}.{}".format(type(self.model).__name__, self.model.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save method of FileStorage"""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """Test reload method of FileStorage"""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(type(self.model).__name__, self.model.id)
        self.assertIn(key, self.storage.all())

    def test_new_with_none(self):
        """Test new method with None as argument"""
        self.storage.new(None)
        self.assertEqual(len(self.storage.all()), 0)

    def test_save_with_no_new_objects(self):
        """Test save method with no new objects"""
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload_with_no_file(self):
        """Test reload method with no file"""
        if os.path.exists('file.json'):
            os.remove('file.json')
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_with_file(self):
        """Test reload method with file"""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.__objects = {}
        self.storage.reload()
        key = "{}.{}".format(type(self.model).__name__, self.model.id)
        self.assertIn(key, self.storage.all())

    def test_new_with_existing_key(self):
        """Test new method with an existing key"""
        key = "{}.{}".format(type(self.model).__name__, self.model.id)
        self.storage.new(self.model)
        self.assertIn(key, self.storage.all())
        old_object = self.storage.all()[key]
        self.storage.new(self.model)
        new_object = self.storage.all()[key]
        self.assertEqual(old_object, new_object)

    def test_save_with_existing_file(self):
        """Test save method with an existing file"""
        self.storage.new(self.model)
        self.storage.save()
        old_modification_time = os.path.getmtime('file.json')
        self.storage.save()
        new_modification_time = os.path.getmtime('file.json')
        self.assertNotEqual(old_modification_time, new_modification_time)

    def test_reload_with_existing_objects(self):
        """Test reload method with existing objects"""
        self.storage.new(self.model)
        self.storage.save()
        old_objects = self.storage.all()
        self.storage.reload()
        new_objects = self.storage.all()
        self.assertEqual(old_objects, new_objects)


if __name__ == '__main__':
    unittest.main()
