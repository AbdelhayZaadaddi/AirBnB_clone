#!/usr/bin/env python3
"""Class Review that inherits from the Basemodel class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class -> BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
