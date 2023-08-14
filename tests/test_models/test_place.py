#!/usr/bin/python3
"""Defines a unittests for BaseModel class."""
import unittest
from models.base_model import BaseModel
from models.place import Place
import os


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cls_place = Place()
        cls.cls_place.name = "dar"
        
    def test_init(self):
        self.assertIsInstance(self.cls_place, Place)
        self.assertTrue(hasattr(self.cls_place, 'id'))
        self.assertTrue(hasattr(self.cls_place, 'created_at'))
        self.assertTrue(hasattr(self.cls_place, 'updated_at'))
        self.assertTrue(hasattr(self.cls_place, 'city_id'))
        self.assertTrue(hasattr(self.cls_place, 'user_id'))
        self.assertTrue(hasattr(self.cls_place, 'name'))
        self.assertTrue(hasattr(self.cls_place, 'description'))
        self.assertTrue(hasattr(self.cls_place, 'number_rooms'))
        self.assertTrue(hasattr(self.cls_place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.cls_place, 'max_guest'))
        self.assertTrue(hasattr(self.cls_place, 'price_by_night'))
        self.assertTrue(hasattr(self.cls_place, 'latitude'))
        self.assertTrue(hasattr(self.cls_place, 'longitude'))
        self.assertTrue(hasattr(self.cls_place, 'amenity_ids'))
        
    def test_is_subclass(self):
        self.assertTrue(issubclass(self.cls_place.__class__, BaseModel), True)

    def test_save(self):
        first_updated_at = self.cls_place.updated_at
        self.cls_place.save()
        self.assertNotEqual(first_updated_at, self.cls_place.updated_at)

    def test_str(self):
        clsname = self.cls_place.__class__.__name__
        clsdict = self.cls_place.__dict__
        ex_str = "[{}] ({}) {}".format(clsname, self.cls_place.id, clsdict)
        self.assertEqual(str(self.cls_place), ex_str)

    def test_to_dict(self):
        cls_user_dict = self.cls_place.to_dict()
        self.assertIsInstance(cls_user_dict, dict)
        self.assertEqual(cls_user_dict['__class__'], 'Place')
        self.assertEqual(str(self.cls_place.id), cls_user_dict['id'])


if __name__ == "__main__":
    unittest.main()
