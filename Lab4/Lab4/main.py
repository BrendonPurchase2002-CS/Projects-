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

    #   season = int(input('Type a number between 1 and 4: '))
    #  seasons(season)

    #grade1 = input("Type in your grade or percentage: ")
    grade = input("Type in your grade or percentage: ")
    grades(grade)

    # fizz = int(input("Please type in a number: "))
    # div1 = int(input('input  divisor 1'))
    # div2 = int(input('input  divisor 2'))
    # fizz_buzz(fizz, div1, div2)

    myinput = input("Please enter a palindrome: ")
    slice_reverse(myinput)
'''
    my_list = [1, 3, 7, 9]
    my_value = 5

    my_list.append(my_value)
    my_list.sort()
    add_to_list(my_value, my_list)
'''

if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
