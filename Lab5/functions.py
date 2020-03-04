# ScriptName: functions.py
# Author: Jason Quinlan

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")


def while_loop(max_number=10):
    my_list = []
    i = 1

    while i <= max_number:
        my_list.append(i)
        i += 1

    print(my_list)


def while_loop2(neg_number):
    my_list1 = []
    i = 1

    while i >= neg_number:
        my_list1.append(i)
        i -= 1

    print(my_list1)


def while_loop3(max_number):
    my_list = []
    i = 1

    while i <= max_number:
        my_list.append(i)
        i -= 1
        accum = 0
        for w in my_list:
            accum = accum + w

    my_list.append(accum)
    print(my_list)


def while_loop4(max_number):
    my_list = []
    i = 1

    while i <= max_number:
        my_list.append(i)
        i -= 1
        accum = 0
        for w in my_list:
            accum =def while_loop3(max_number):
    my_list = []
    i = 1

    while i <= max_number:
        my_list.append(i)
        i -= 1
        accum = 0
        for w in my_list:
            accum = accum + w accum + w
        if i < -12 or i > 12:
            break

    my_list.append(accum)
    print(my_list)


'''def while_loop5(max_number, even):
    my_list = []
    i = 1

    while i <= max_number:
        my_list.append(i)
        i += 1
        accum = 0

        for w in my_list:
            accum = accum + w
        if i < -12 or i > 12:

            break
        elif i % 2 == 0:
            i += 1
            continue

    my_list.append(accum)
    print(my_list)

'''


def while_loop5(max_number=10, even=False):
    my_list = []
    accum = 0
    i = 1

    if max_number < 0:
        while i >= max_number:
            if even and i % 2 == 1:
                i -= 1
                continue

            my_list.append(i)
            accum -= i
            i -= 1

            if i < -12:
                break
    else:
        while i <= max_number:
            if even and i % 2 == 1:
                i += 1
                continue

            my_list.append(i)
            accum += i
            i += 1

            if i > 12:
                break

    my_list.append(accum)
    print(my_list)


def while_loop6(max_number=10, even=False, boolean="False"):
    my_list = []
    accum = 0
    factorial = 1
    i = 1

    if max_number < 0:
        while i >= max_number:
            if even and i % 2 == 1:
                i -= 1
                continue

            my_list.append(i)
            accum -= i
            i -= 1

            if i < -12:
                break

    elif max_number > 0:

        while i <= max_number:
            my_list = my_list + [i]

            factorial = factorial * i
            accum += i
            i += 1
            if i > 12:
                break

    else:
        while i <= max_number:
            if even and i % 2 == 1:
                i += 1
                continue

            my_list.append(i)
            accum += i
            i += 1

            if i > 12:
                break

    my_list.append(accum)
    my_list.append(factorial)
    print(my_list)
