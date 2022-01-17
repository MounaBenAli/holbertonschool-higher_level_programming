#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    try:
        res = [i / j for i, j in zip(my_list_1, my_list_2)]
        print(str(res))

    except ZeroDivisionError:
        print("division by 0")

    except TypeError:
        print("wrong type")

    except IndexError:
        print("out of range")
    return res
