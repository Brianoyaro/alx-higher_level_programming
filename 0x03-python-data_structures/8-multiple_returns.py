#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    if (ln == 0):
        return (ln, 'None')
    else:
        return (ln, sentence[0])
