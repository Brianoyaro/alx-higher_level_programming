#!/usr/bin/python3
"""my rebel int module
"""


class MyInt(int):
    """MyInt class
    """
    #def __init__(self, i):
        #self.i = i

    def __eq__(self, value, /):
        """reverses the equal operator
        """
        return False
    def __ne__(self, value, /):
        """reverses the not equal operator
        """
        return True
