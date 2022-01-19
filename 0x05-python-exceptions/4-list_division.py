#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(0, list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            x = 0
        except TypeError:
            print("wrong type")
            x = 0
        except IndexError:
            print("out of range")
            x = 0
        finally:
            res.append(x)
    return res
