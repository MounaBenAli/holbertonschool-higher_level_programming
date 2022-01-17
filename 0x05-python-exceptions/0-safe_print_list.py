#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        index = 0
        for x in range(x):
            print('{}'.format(my_list[x]), end="")
            index += 1
    except IndexError:
        pass
    finally:
        print()
        return (index)
