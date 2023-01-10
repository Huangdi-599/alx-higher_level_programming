#!/usr/bin/python3
"""Defines a class Student."""

class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialization a new Student.
        Parameters:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student."""
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for items in attrs:
            if hasattr(self, items):
                my_dict[items] = getattr(self, items)
        return my_dict
