#!/usr/bin/env python3
"""Class User inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class -> BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
