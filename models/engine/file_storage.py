#!/usr/bin/python3
'''
FileStorage module Containig the FileStorage class
'''

import json


class FileStorage:
    '''FileStorage class'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects and saves them to a JSON file"""
        json_object = {}

        for key in FileStorage.__objects:
            json_object[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        """Deserializes objects from a JSON file
        and loads them into the dictionary"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)

                for key, value in data.items():
                    class_name = value["__class__"]

                    if class_name in globals():
                        class_obj = globals()[class_name]
                        print(class_obj)
                        del value["__class__"]
                        obj_instance = class_obj(**value)
                        FileStorage.__objects[key] = obj_instance
                    else:
                        from models.base_model import BaseModel
                        from models.user import User
                        from models.state import Satate
                        from models.city import City
                        from models.amenity import Amenity
                        from models.place import Place
                        from models.review import Review

                        obj = eval(key.split(".")[0])(**value)
                        FileStorage.__objects[key] = obj

        except FileNotFoundError:
            return
