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
        storage = FileStorage()
        instances_dic = storage.all()
        base_a = BaseModel()
        base_a.name = "base"
        storage.new(base_a)
        key = base_a.__class__.__name__ + "." + str(base_a.id)
        self.assertIsNotNone(instances_dic[key])

    def test_attributes(self):
        storage = FileStorage()
        self.assertTrue(hasattr(storage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(storage, '_FileStorage__objects'))
    
    def test_reload_nonexistent_file(self):
        
        nonexistent_storage = FileStorage()
        nonexistent_storage.reload()
        self.assertEqual(nonexistent_storage.all(), {})

    def test_save_reload(self):
        storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(storage.reload(), None)

    def test_all(self):
        storage = FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)


if __name__ == '__main__':
    unittest.main()
