#!/usr/bin/python3
"""Defines a unittests for BaseModel class."""
import unittest
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):

    def test_save(self):
        first_updated_at = self.cls_base.updated_at
        self.cls_base.save()
        self.assertNotEqual(first_updated_at, self.cls_base.updated_at)

    def test_str(self):
        clsname = self.cls_base.__class__.__name__
        clsdict = self.cls_base.__dict__
        ex_str = "[{}] ({}) {}".format(clsname, self.cls_base.id, clsdict)
        self.assertEqual(str(self.cls_base), ex_str)

    def test_to_dict(self):
        cls_base_dict = self.cls_base.to_dict()
        self.assertIsInstance(cls_base_dict, dict)
        self.assertEqual(cls_base_dict['__class__'], 'BaseModel')
        self.assertEqual(str(self.cls_base.id), cls_base_dict['id'])
        
    def test_init(self):
        self.assertIsInstance(self.cls_base, BaseModel)
        self.assertTrue(hasattr(self.cls_base, 'id'))
        self.assertTrue(hasattr(self.cls_base, 'created_at'))
        self.assertTrue(hasattr(self.cls_base, 'updated_at'))


if __name__ == "__main__":
    unittest.main()
