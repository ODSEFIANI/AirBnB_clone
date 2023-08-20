#!/usr/bin/python3
"""Defines a unittests for BaseModel class."""
import unittest
from models.base_model import BaseModel
from models.city import City
import os


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cls_city = City()
        cls.cls_city.state_id = "1234"
        cls.cls_city.name = "name"
        
    def test_init(self):
        self.assertIsInstance(self.cls_city, City)
        self.assertTrue(hasattr(self.cls_city, 'id'))
        self.assertTrue(hasattr(self.cls_city, 'state_id'))
        self.assertTrue(hasattr(self.cls_city, 'name'))
        self.assertTrue(hasattr(self.cls_city, 'created_at'))
        self.assertTrue(hasattr(self.cls_city, 'updated_at'))
        
    def test_is_subclass(self):
        self.assertTrue(issubclass(self.cls_city.__class__, BaseModel), True)

    def test_save(self):
        first_updated_at = self.cls_city.updated_at
        self.cls_city.save()
        self.assertNotEqual(first_updated_at, self.cls_city.updated_at)

    def test_str(self):
        clsname = self.cls_city.__class__.__name__
        clsdict = self.cls_city.__dict__
        ex_str = "[{}] ({}) {}".format(clsname, self.cls_city.id, clsdict)
        self.assertEqual(str(self.cls_city), ex_str)

    def test_to_dict(self):
        cls_user_dict = self.cls_city.to_dict()
        self.assertIsInstance(cls_user_dict, dict)
        self.assertEqual(cls_user_dict['__class__'], 'City')
        self.assertEqual(str(self.cls_city.id), cls_user_dict['id'])


if __name__ == "__main__":
    unittest.main()
