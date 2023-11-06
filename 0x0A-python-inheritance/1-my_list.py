#!/usr/bin/python3
"""MyList module
"""


class MyList(list):
    """MyList class

    iherits from class list
    """
    def print_sorted(self):
        """prints each class instance in sorted order
        """
        print(sorted(self))
