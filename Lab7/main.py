# ScriptName: main.py
# Author: Jason Quinlan

# template for calling functions in another file

# import functions from other files - different options
# from functions import print_function
# import functions - when you use this you need to call the function using 'functions.<function_name>'
# this option imports all functions, using '*'
from functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    print_function()

    # print(is_stairs([ 2, 3, 4, 5]))
    # print(is_stairs([8, 7, 6]))
    # print(is_stairs([2, 3, 5]))
    # print(is_stairs([2, 3, 2]))
    # print(is_stairs([4]))
    # print(is_stairs2(["a", "b", "c"]))
    # print(is_stairs2(["c", "b", "a"]))
    # print(is_stairs2(["a", "B", "c"]))
    # print(is_stairs2(["a", "b", "C"]))
    # print(is_stairs2(["c", "B", "a"]))
    # print(is_stairs2(["C", "b", "a"]))
    # print(factorial(3))
    # print(factorial(1))
    # print(factorial(0))
    # print(factorial(40))
    print(test(['d', 'e', 'g']))




if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
