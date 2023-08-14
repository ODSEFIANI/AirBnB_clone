#!/usr/bin/python3
"""
Review Model
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ a class thet inherits from BaseModel """

    place_id = ""
    user_id = ""
    text = ""