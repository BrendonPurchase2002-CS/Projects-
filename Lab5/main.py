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

    # max_number = int(input("input a maximum number: "))
    #while_loop(5)

    # neg_number = int(input("Please enter a positive/negative number: "))
    #while_loops(-8)

    while_loop6(12, False, True)


if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
