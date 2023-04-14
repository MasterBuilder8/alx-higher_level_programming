#!/usr/bin/python3
"""
Contains the function "append_write"
"""

def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)

    Returns: number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
