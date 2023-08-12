"""
Unittest for BaseModel Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""


import unittest
from models import base_model
BaseModel = base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """
    tests for models/base_model.py
    """

    def test_init(self):
        """
        tests if an instance is created
        """
        obj = BaseModel()
        self.assertTrue(isinstance(obj, BaseModel))
