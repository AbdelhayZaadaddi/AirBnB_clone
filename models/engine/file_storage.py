#!/usr/bin/python3

import json

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):

        return FileStorage.__objects

    def new(self, obj):

        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):

        serialized_objects = {}

        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)
        
    def reload(self):
        try:
            pass
        except FileNotFoundError:
            pass