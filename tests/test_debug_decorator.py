"""test_debug_decorator is used to test the debug decorator located in
tools/debug_decorator.py"""

import sys

sys.path.insert(0, '/Volumes/T7/Github/hackerrank/')

from tools.debug_decorator import debug

@debug
def hello_world():
    """This function prints "hello world".
    """

    print("hello World")


if __name__ == '__main__':
    hello_world()
