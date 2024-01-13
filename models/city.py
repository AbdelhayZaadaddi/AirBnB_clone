#!/usr/bin/env python3
"""class City that inherits from BaseModel class"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class -> BaseModel"""
    state_id = ""
    name = ""
