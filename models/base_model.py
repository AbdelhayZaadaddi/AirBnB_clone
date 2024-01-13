#!/usr/bin/env python3
'''Base module class for class to inherit from'''

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''Defines methods for class to inherit from'''
    def __init__(self, *args, **kwargs):
        '''Initializes instances'''
        timeformt = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, timeformt)
                    setattr(self, key, value)
                self.updated_at = datetime.now()
            self.id = kwargs.get('id')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        '''string representation of the object'''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Updates with the current time'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Converts the object's attributes to a dictionary'''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
