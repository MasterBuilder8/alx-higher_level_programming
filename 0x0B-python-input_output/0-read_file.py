#!/usr/bin/python3
"""
defining a function
"""

def read_file(filename=""):
    """function that reads a text file"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
