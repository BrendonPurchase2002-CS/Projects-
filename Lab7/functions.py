# ScriptName: functions.py
# Author: Jason Quinlan

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")


# A
def is_stairs(s):
    ascend = False
    if len(s) < 2:
        return False
    if s[0] < s[1]:
        ascend = True
    for index in range(2, len(s)):
        if ascend:
            if s[index - 1] == s[index] - 1:
                continue
            else:
                return False
        else:  # descending order
            if s[index - 1] == s[index] + 1:
                continue
            else:
                return False
    return True


# B
def is_stairs2(s):
    ascend = False
    if len(s) < 2:
        return False
    if s[0].lower() < s[1].lower():
        ascend = True
    for index in range(2, len(s)):
        if ascend:
            if s[index - 1].lower() == s[index] - 1:
                continue
            else:
                return False
        else:  # descending order
            if s[index - 1] == s[index] + 1:
                continue
            else:
                return False
    return True



def test(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    tebahpla = 'zyxwvutsrqponmlkjihgfedcba'
    for i in range(1, len(s)):
        # list = ['a', 'b', 'c']
        if alphabet[alphabet.index(s[i - 1].lower()) + 1] == s[i].lower():
            continue
        if tebahpla[tebahpla.index(s[i - 1].lower()) + 1] == s[i].lower():
            continue
        else:
            return False
    return True


# C
def factorial(n):
    for i in range(1, n + 1):
        if n == 1:
            return 1
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


def gremlins(name):
    return
