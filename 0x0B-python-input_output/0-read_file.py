#!/usr/bin/python3
"""
defining a function
"""

def read_file(filename=""):
    """function that reads a text file and prints to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
