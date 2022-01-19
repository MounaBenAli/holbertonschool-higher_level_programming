#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        i = fct(*args)
        return i
    except Exception as e:

        import sys
        print('Exception : {}'.format(e), file=sys.stderr)
        return None
