# ScriptName: functions.py
# Author: Brendon Purchase 
# StudentNumber: 119473576

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")


def seasons(my_input):
    seasons_list = ["Winter", "Spring", "Summer", "Autumn"]
    if my_input == 1:
        print(seasons_list[0])
    elif my_input == 2:
        print(seasons_list[1])
    elif my_input == 3:
        print(seasons_list[2])
    elif my_input == 4:
        print(seasons_list[3])
    else:
        print('uh oh!')
    print(seasons_list[my_input - 1])


def grades(value):
    if value.upper() in ["A", "B", "C", "D", "E", "F"]:
        value = value.upper()
        if value == 'A':
            print("85-100")
        elif value == 'B':
            print("70-84")
        elif value == 'C':
            print("55-69")
        elif value == 'D':
            print("40-54")
        elif value == 'E':
            print("25-39")
        elif value == 'F':
            print("0-24")
    else:
        value = int(value)
        if value >= 85 >= 100:
            print('A')
        elif 84 >= value >= 70:
            print('B')
        elif 69 >= value >= 55:
            print('C')
        elif 54 >= value >= 40:
            print('D')
        elif 39 >= value >= 25:
            print('E')
        elif 24 >= value >= 0:
            print('F')
        else:
            print('X')


def fizz_buzz(integer, divisor_1, divisor_2):
    # if integer % 3 == 0 and integer % 4 == 0:
    #     print("FizzBuzz")
    # elif integer % 3 == 0:
    #     print("Fizz")
    # elif integer % 4 == 0:
    #     print("Buzz")
    if divisor_1 % 3 == 0 and divisor_2 % 4 == 0:
        print("FizzBuzz")
    elif divisor_1 % 3 == 0:
        print("Fizz")
    elif divisor_2 % 4 == 0:
        print("Buzz")
    else:
        print('nope!')


def slice_reverse(myinput):
    if myinput == myinput[::-1]:
        print("True")
    else:
        print("False")


def add_to_list(my_value, my_list):
    print(my_list)

# def add_to_list(value, list):
#   return
