#!/usr/bin/python3
"""my rebel int module
"""


class MyInt(int):
    """MyInt class
    """
    def __eq__(self, value, /):
        """reverses the equal operator
        """
        return False

    def __ne__(self, value, /):
        """reverses the not equal operator
        """
        return True
