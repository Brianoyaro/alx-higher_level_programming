#!/usr/bin/python3
"""
    module that prints a user's name
"""
def say_my_name(first_name, last_name=""):
    """
        function that says a user's name

        Args:
            first_name: first parameter
            second_name(optional): second parameter

        Return:
            string saying user's name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
