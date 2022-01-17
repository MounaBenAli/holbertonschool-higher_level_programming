#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    res = 0
    try:
        res = [i / j for i, j in zip(my_list_1, my_list_2)]
        print(str(res))

    except ZeroDivisionError:
        print("division by 0")
        res = 0
    except TypeError:
        print("wrong type")
        res = 0
    except IndexError:
        print("out of range")
        res = 0
    finally:
            new.append(res)
    return res
