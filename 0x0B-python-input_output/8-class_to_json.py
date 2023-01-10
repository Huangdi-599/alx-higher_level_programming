#!/usr/bin/python3
"""Function that returns a dictionary description"""

def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
