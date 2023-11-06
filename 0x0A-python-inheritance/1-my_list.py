#!/usr/bin/python3
"""MyList module
"""


class MyList(list):
    """MyList class

    iherits from class list
    """

    def __init__(self):
        """initialises each object instance
        """
        super().__init__(self)

    def print_sorted(self):
        """prints each class instance in sorted order
        """
        print(sorted(self))
