# ScriptName: functions.py
# Author: Jason Quinlan

# template for calling functions in another file

import math


def print_function():
    print("I'm in another file :)")


def three_numbers(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        print("True!")
    else:
        print('False!')


def seasons(number):
    if number == 1:
        print('spring')
    elif number == 2:
        print('summer')
    elif number == 3:
        print('autumn')
    elif number == 4:
        print('winter')
    else:
        print("ERROR!")


def grades(number):
    if number >= 85:
        print('A')
    elif 84 >= number >= 70:
        print('B')
    elif 69 >= number >= 55:
        print('C')
    elif 54 >= number >= 40:
        print('D')
    elif 39 >= number >= 25:
        print('E')
    elif 24 >= number >= 0:
        print('F')
    else:
        print('X')


def equal_numbers(number1, number2):
    if number1 == number2:
        print(math.sqrt(number1))
    else:
        # print(math.sqrt(number1)) and print(math.sqrt(number2))
        print(number1 ** 2, number2 ** 2)

def fizz_buzz(integer):
    if integer % 3 == 0 and integer % 4 ==0:
            print("FizzBuzz")
    elif integer % 3 == 0:
            print("Fizz")
    elif integer % 4 == 0:
            print("Buzz")

    else:
        print('nope!')