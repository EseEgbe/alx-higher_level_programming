#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        result = fct(*args)
    except Exception as exception:
        sys.stderr.write("Exception: {}\n".format(exception))
        result = None

    return result
