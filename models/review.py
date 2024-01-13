#!/usr/bin/env python3
"""Class Review that inherits from the Basemodel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class"""
    place_id = ""
    user_id = ""
    text = ""
