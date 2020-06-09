#!/usr/bin/python3
""" Module for a Class Base"""


import json


class Base:
    """This is a Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is a method initializer

            Args:
                id (int, optional): value to set id of the object.
                Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
           (Serialization)

            Args:
                list_dictionaries (list): A list of dictinaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file:

            Args:
                list_objs (list): A list of objects
        """
        filename = "{}.json".format(cls.__name__)
        list_dicts = []
        with open(filename, mode="w", encoding="utf-8") as my_file:
            if list_objs is None:
                my_file.write("[]")
            else:
                list_dicts = [item.to_dictionary() for item in list_objs]
                my_file.write(cls.to_json_string(list_dicts))

    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

            Args:
                json_string (string): a string representing a list of
                dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as my_file:
                l_dictionaries = Base.from_json_string(my_file.read())
                return [cls.create(**item) for item in l_dictionaries]
        except IOError:
            return []
