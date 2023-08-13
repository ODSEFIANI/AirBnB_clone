#!/usr/bin/python3
"""test 12
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import os
import json



class TestFileStorage(unittest.TestCase):

    def test_new(self):
        user = BaseModel()
        self.storage.new(user)
        all_objects = self.storage.all()
        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertTrue(key in all_objects)

    def test_attributes(self):
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))
    
    def test_reload_nonexistent_file(self):
        
        nonexistent_storage = FileStorage()
        nonexistent_storage.reload()
        self.assertEqual(nonexistent_storage.all(), {})

    def test_save_reload(self):
        user = BaseModel()
        self.storage.new(user)
        self.storage.save()
        file_path = self.storage._FileStorage__file_path
        self.assertTrue(os.path.exists(file_path))

        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertTrue(key in all_objects)

    def test_all(self):
        storage = FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)


if __name__ == '__main__':
    unittest.main()