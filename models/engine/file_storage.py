#!/usr/bin/python3
""" Class FileStorage """

import models
import json
import os


class Objects(dict):
    """class object"""

    def __getitem__(self, key):
        """get item"""
        try:
            return super(Objects, self).__getitem__(key)
        except Exception as e:
            raise Exception("** no instance found **")

    def pop(self, key):
        """pop item"""
        try:
            return super(Objects, self).pop(key)
        except Exception as e:
            raise Exception("** no instance found **")


class FileStorage:
    """Serializes instances to a JSON file & vice versa
    """

    __file_path = "file.json"
    __objects = Objects()

    def __init__(self):
        """Empty constructor"""
        pass

    def all(self):
        """Returns the __objects from this file
        """
        return FileStorage.__objects

    def new(self, obj):
        """Adds the new object to the __objects variable
        Args:
            @obj: new object
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """ serializes __objects to the json file
        """
        obj_dict = {
            key: value.to_dict()
            for key, value in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """ if (__file_path) exists deserializes JSON file to __objects
            elif , do nothing. If the file not exist,
        """
        with open(FileStorage.__file_path, "r") as json_file:
            obj_dict = json.load(json_file)
