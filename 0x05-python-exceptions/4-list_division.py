#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ls = []
    for i in range(list_length):
        try:
            val = my_list_1[i] / my_list_2[i]
            ls.append(val)
        except ZeroDivisionError:
            print("division by 0")
            ls.append(0)
        except TypeError:
            print("wrong type")
            ls.append(0)
        except IndexError:
            print("out of range")
            ls.append(0)
        finally:
            continue
    return ls
