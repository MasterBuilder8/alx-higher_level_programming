#!/usr/bin/python3
"""a module that prints a list in ascending order"""


class MyList(list):
    """child class MyList from base class list
    """

    def print_sorted(self):
        """print a list in ascending order
        sort a list then print in ascending order
        """

        if issubclass(MyList, list):
            print(sorted(self))
