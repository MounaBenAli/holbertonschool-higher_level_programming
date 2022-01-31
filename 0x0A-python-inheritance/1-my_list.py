#!/usr/bin/python3
"The is a module that defines a derived class named MyList from the base list"


class MyList(list):
    """A class named MyList
    Attributes:
    attr1(print_sorted): prints sorted list"""
    def print_sorted(self):
        """Prints instance"""
        print(sorted(self))
