#!/usr/bin/python3
"""Defines a unittests for BaseModel class."""
import unittest
from models.base_model import BaseModel
from models.review import Review
import os


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cls_review = Review()
        cls.cls_review.text = "texte"
        
    def test_init(self):
        self.assertIsInstance(self.cls_review, Review)
        self.assertTrue(hasattr(self.cls_review, 'id'))
        self.assertTrue(hasattr(self.cls_review, 'created_at'))
        self.assertTrue(hasattr(self.cls_review, 'updated_at'))
        self.assertTrue(hasattr(self.cls_review, 'place_id'))
        self.assertTrue(hasattr(self.cls_review, 'user_id'))
        self.assertTrue(hasattr(self.cls_review, 'text'))
        
    def test_is_subclass(self):
        self.assertTrue(issubclass(self.cls_review.__class__, BaseModel), True)

    def test_save(self):
        first_updated_at = self.cls_review.updated_at
        self.cls_review.save()
        self.assertNotEqual(first_updated_at, self.cls_review.updated_at)

    def test_str(self):
        clsname = self.cls_review.__class__.__name__
        clsdict = self.cls_review.__dict__
        ex_str = "[{}] ({}) {}".format(clsname, self.cls_review.id, clsdict)
        self.assertEqual(str(self.cls_review), ex_str)

    def test_to_dict(self):
        cls_user_dict = self.cls_review.to_dict()
        self.assertIsInstance(cls_user_dict, dict)
        self.assertEqual(cls_user_dict['__class__'], 'Review')
        self.assertEqual(str(self.cls_review.id), cls_user_dict['id'])


if __name__ == "__main__":
    unittest.main()
