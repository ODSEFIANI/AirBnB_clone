#!/usr/bin/python3
"""
Unittest for BaseModel Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""

import unittest
from models import base_model
from datetime import datetime
BaseModel = base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """
    tests for models/base_model.py
    """

    def test_init(self):
        """
        tests if an instance is created
        """
        new = BaseModel()

        """ check if it have methods """
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        """existince"""
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))

        """type test"""
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
