#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        result = fct(*args)
    except Exception as Exception:
        sys.stderr.write("Exception: {}\n".format(Exception))
        result = None

    return result
