#!/usr/bin/python3
"""Python Function to append string to a file"""

def append_write(filename="", text=""):
    """Return an appended file with the textfile
    Parameters: filename : the name of the file to be edited
                text: the text content to be added to the file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
