#!/usr/bin/python3
import sys

args = sys.argv[1:]

num_args = len(args)

if num_args == 0:
    print("Number of argument(s): 0.")
    print(".")
else:
    print("Number of argument(s): {}.".format(num_args))
    print(":")
    for i, arg in enumerate(args):
        print("{}: {}".format(i+1, arg))

