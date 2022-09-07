#!/usr/bin/python3
"""Defines FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """stores obj in __objects"""
        cl_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(cl_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        new_dict = FileStorage.__objects
        new_dict = {key: value.to_dict() for key, value in new_dict.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cl_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cl_name)(**obj))
        except FileNotFoundError:
            return
