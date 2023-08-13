#!/usr/bin/python3
""" unittt test for basessss """
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
import sys


class BaseModelTestCase(unittest.TestCase):
    """ classss for base testtt """
    def test_basemodel_init(self):
        """ class for base test """
        new = BaseModel()

        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))

        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
