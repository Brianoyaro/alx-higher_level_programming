#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    ln = len(my_list)
    if ((idx < 0) or (idx >= ln)):
        return my_list
    else:
        tmp = my_list[idx]
        my_list.remove(tmp)
    return my_list
