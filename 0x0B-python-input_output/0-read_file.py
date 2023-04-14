#!/usr/bin/python3
"""
defining a function
"""


def read_file(filename=""):
    """reads a text file(UTF8) and prints to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
