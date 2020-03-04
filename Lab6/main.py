# ScriptName: main.py
# Author: Jason Quinlan

# template for calling functions in another file

# import functions from other files - different options
# from functions import print_function
# import functions - when you use this you need to call the function using 'functions.<function_name>'
# this option imports all functions, using '*'
import functions
from functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    print_function()

    # test count
    #   print(count([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 4))
    #  print(count([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 8))
    #  print(count("hello", "l"))
    #  print(count("hello", "h"))
    #  print(count("hello", "w"))

    # print(index([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 4)) #3
    #  print(index([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 8)) #-1
    # print(index("hello", "l")) #2
    # print(index("hello", "h")) #0
    # print(index("hello", "w")) #-1

    #print(get_value("hello", 1,))  # e
    #print(get_value("almond", 4, ))  # n
    #print(get_value("glazing", 5, ))  # n

    print(insert("hello", 1, "a"))  # hallo
    print(insert("almond", 4, "k"))  # almokd
    print(insert("glazing", 5, "j"))  # glazijg
    print(insert("leg", 4, "h"))

    #print(value_in_list("hello", "o"))
    #print(value_in_list("almond", "n"))
    #print(value_in_list("glazing", "f"))
    #print(value_in_list("egg", "g"))

    #print(concat("glazed", "ham"))
    #print(concat("baked", "beans"))
    #print(concat("peanut", "butter"))

    # print(remove("hello", "h"))
    # print(remove("egg", "e"))
    # print(remove("aubergine", "i"))




if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
