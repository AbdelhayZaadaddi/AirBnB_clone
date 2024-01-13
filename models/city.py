#!/usr/bin/env python3
'''class City that inherits from BaseModel'''

from models.base_model import BaseModel


class City(BaseModel):
    '''City class'''
    state_id = ""
    name = ""
