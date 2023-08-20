#!/usr/bin/python3
"""Defines a unittests for BaseModel class."""
import unittest
from models.base_model import BaseModel
from models.user import User
import os


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cls_user = User()
        cls.cls_user.email = "airbnb@gmail.com"
        cls.cls_user.password = "root"
        
    def test_init(self):
        self.assertIsInstance(self.cls_user, User)
        self.assertTrue(hasattr(self.cls_user, 'id'))
        self.assertTrue(hasattr(self.cls_user, 'email'))
        self.assertTrue(hasattr(self.cls_user, 'password'))
        self.assertTrue(hasattr(self.cls_user, 'first_name'))
        self.assertTrue(hasattr(self.cls_user, 'last_name'))
        self.assertTrue(hasattr(self.cls_user, 'created_at'))
        self.assertTrue(hasattr(self.cls_user, 'updated_at'))
        
    def test_is_subclass(self):
        self.assertTrue(issubclass(self.cls_user.__class__, BaseModel), True)

    def test_save(self):
        first_updated_at = self.cls_user.updated_at
        self.cls_user.save()
        self.assertNotEqual(first_updated_at, self.cls_user.updated_at)

    def test_str(self):
        clsname = self.cls_user.__class__.__name__
        clsdict = self.cls_user.__dict__
        ex_str = "[{}] ({}) {}".format(clsname, self.cls_user.id, clsdict)
        self.assertEqual(str(self.cls_user), ex_str)

    def test_to_dict(self):
        cls_user_dict = self.cls_user.to_dict()
        self.assertIsInstance(cls_user_dict, dict)
        self.assertEqual(cls_user_dict['__class__'], 'User')
        self.assertEqual(str(self.cls_user.id), cls_user_dict['id'])


if __name__ == "__main__":
    unittest.main()
