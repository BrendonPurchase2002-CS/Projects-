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
    hexToBinaryTable = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                        '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
                        'E': '1110', 'F': '1111'}
    print(hailStone(43))

    print(hexToBinary('ABC12', hexToBinaryTable))

if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()



