#!/usr/bin/python3
""" Module for BaseClass, from which classes inherit"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """ Defines methods for class to inherit from"""
    def __init__(self, *args, **kwargs):
        """ Initializes the instances"""
        sformat = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, sformat)
                    setattr(self, key, value)
            self.id = kwargs.get('id')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ String representation of the object"""
        class_name = self.__class__.__name__
        dicts = self.__dict__
        id = self.id
        return ("[{}] ({}) ({})".format(class_name, id, dicts))

    def to_dict(self):
        """ Converts the Object's attributes to a dictionary"""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return (dict)

    def save(self):
        """ Updates time with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()
