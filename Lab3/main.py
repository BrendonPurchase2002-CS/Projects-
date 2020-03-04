# ScriptName: main.py
# Author: Jason Quinlan

# template for calling functions in another file

# import functions from other files - different options
#   from functions import print_function
# import functions - when you use this you need to call the function using 'functions.<function_name>'
# this option imports all functions, using '*'
from functions import *
import math

def main():
    for i in range(15):
        fizz_buzz(i)

    '''
    number1 = int(input('Please enter number 1:'))
    number2 = int(input('Please enter number 2:'))
    equal_numbers(number1, number2)
    '''
    """
    Call the functions defined in the functions.py file
    """
    '''
    num1 = int(input("Please enter a number:"))
    num2 = int(input("Please enter another number:"))
    num3 = int(input("Please enter one more number:"))

    three_numbers(num1, num2, num3)
'''
'''
number = int(input('Please enter a number:'))
seasons(number)
'''
'''
number = int(input('Please enter your grade:'))
grades(number)
'''
    # integer = int(input("Please enter a number:"))






if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()



