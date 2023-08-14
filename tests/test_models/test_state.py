#!/usr/bin/python3
"""Defines a unittests for BaseModel class."""
import unittest
from models.base_model import BaseModel
from models.state import State
import os


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cls_state = State()
        cls.cls_state.name = "casa"
        
    def test_init(self):
        self.assertIsInstance(self.cls_state, State)
        self.assertTrue(hasattr(self.cls_state, 'id'))
        self.assertTrue(hasattr(self.cls_state, 'name'))
        self.assertTrue(hasattr(self.cls_state, 'created_at'))
        self.assertTrue(hasattr(self.cls_state, 'updated_at'))
        
    def test_is_subclass(self):
        self.assertTrue(issubclass(self.cls_state.__class__, BaseModel), True)

    def test_save(self):
        first_updated_at = self.cls_state.updated_at
        self.cls_state.save()
        self.assertNotEqual(first_updated_at, self.cls_state.updated_at)

    def test_str(self):
        clsname = self.cls_state.__class__.__name__
        clsdict = self.cls_state.__dict__
        ex_str = "[{}] ({}) {}".format(clsname, self.cls_state.id, clsdict)
        self.assertEqual(str(self.cls_state), ex_str)

    def test_to_dict(self):
        cls_user_dict = self.cls_state.to_dict()
        self.assertIsInstance(cls_user_dict, dict)
        self.assertEqual(cls_user_dict['__class__'], 'State')
        self.assertEqual(str(self.cls_state.id), cls_user_dict['id'])


if __name__ == "__main__":
    unittest.main()
