#!/usr/bin/python3
"""
    module that prints a text with 2 new lines\
    after each of these characters: ., ? and :
"""
def text_indentation(text):
    """
        function that text idents

        Args:
            text: only argument

        Return:
            Text which has been delimeter idented using ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        start = ""
        final = ""
        for i in text:
            if i in ".:?":
                final += start.strip() + i + '\n\n'
                start = ""
            else:
                start += i
        final += start.strip()
        print(final)
