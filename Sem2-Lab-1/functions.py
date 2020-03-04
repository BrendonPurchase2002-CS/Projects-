# ScriptName: functions.py
# Author: Jason Quinlan

# template for calling functions in another file


def a_function():
    return ("I'm in another file :)")


def three_numbers(number_1, number_2, number_3):
    if number_1 == number_2 == number_3:
        return ("True")
    else:
        return ("False")


def seasons(number):
    season_dict = {1: "Spring", 2: "Summer", 3: "Autumn", 4: "Winter"}
    try:
        if 0 < number < 5:
            return season_dict[number]
        else:
            return ('Number entered, 5, is outside of input values')
    except:
        return ('Input value must be a number')


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


def slice_reverse(myinput):
    if myinput == myinput[::-1]:
        print("True")
    else:
        print("False")
