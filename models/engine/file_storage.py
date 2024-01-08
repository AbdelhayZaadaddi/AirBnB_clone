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
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    obj_instance = class_obj(**value)
                    FileStorage.__objects[key] = obj_instance

        except FileNotFoundError:
            pass