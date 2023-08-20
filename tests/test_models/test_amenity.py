#!/usr/bin/python3
"""Defines a unittests for BaseModel class."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import os


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cls_amenity = Amenity()
        cls.cls_amenity.name = "ameni"
        
    def test_init(self):
        self.assertIsInstance(self.cls_amenity, Amenity)
        self.assertTrue(hasattr(self.cls_amenity, 'id'))
        self.assertTrue(hasattr(self.cls_amenity, 'name'))
        self.assertTrue(hasattr(self.cls_amenity, 'created_at'))
        self.assertTrue(hasattr(self.cls_amenity, 'updated_at'))
        
    def test_is_subclass(self):
        self.assertTrue(issubclass(self.cls_amenity.__class__, BaseModel), True)

    def test_save(self):
        first_updated_at = self.cls_amenity.updated_at
        self.cls_amenity.save()
        self.assertNotEqual(first_updated_at, self.cls_amenity.updated_at)

    def test_str(self):
        clsname = self.cls_amenity.__class__.__name__
        clsdict = self.cls_amenity.__dict__
        ex_str = "[{}] ({}) {}".format(clsname, self.cls_amenity.id, clsdict)
        self.assertEqual(str(self.cls_amenity), ex_str)

    def test_to_dict(self):
        cls_user_dict = self.cls_amenity.to_dict()
        self.assertIsInstance(cls_user_dict, dict)
        self.assertEqual(cls_user_dict['__class__'], 'Amenity')
        self.assertEqual(str(self.cls_amenity.id), cls_user_dict['id'])


if __name__ == "__main__":
    unittest.main()
