# ScriptName: functions.py
# Author: Brendon Purchase 119473576

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")


def count(list, value):
    '''
    function - count how many times <value> occurs in <list>
    :param list: - <list> input
    :param value: - <value> to search for
    :return:
    '''
    # set counter
    i = 0
    # accumulator to count how many times <value> occurs
    # set to zero to cover no <value> in <list>
    num_values = 0
    # loop over the length of the <list>
    while i < len(list):
        # if <value> and <list> index i are the same
        if list[i] == value:
            # increment the accumulator
            num_values += 1
        # increment the counter
        i += 1
    # return how many times <value> occurs in <list>
    return num_values


def index(list, value):
    '''
    function - return the first index that <value> occurs in <list>
    :param list: - <list> input
    :param value: - <value> to search for
    :return:
    '''
    # counter
    i = 0
    # accumulator to count the first index that <value> occurs
    # set to zero to cover no <value> in <list>
    # num_index = 0
    # loop over the length of list
    while i < len(list):
        if list[i] == value:
            # COUNTS INDEX
            return i
            # num_index += 1
        i += 1
        # RETURNS INDEX
    return -1


def get_value(list, index):
    '''
    function - return the value that occurs in <list> at <index>
    :param list: - list input
    :param index: - value to return
    :return:
    '''
    # set counter

    i = 0
    while index < len(list):
        if i == index:
            return list[i]
        i += 1


def insert(lst, index, value):
    '''
    function - function to return <list> ,after you have added <value> at <index>
    :param lst: - list input
    :param index: - specifies where <value> is added
    :param value: - value to add
    :return:
    '''
    i = 0
    lst = list(lst)
    while i < len(lst):
        if i == index:
            lst[i] = value
            return ''.join(lst)

        i += 1

    lst.append(value)
    return ''.join(lst)


def value_in_list(mylist, value):
    '''
    function - function to return True or False if <value> occurs in <list>
    :param mylist: -  list input
    :param value: - value which may occur
    :return:
    '''
    i = 0
    while i < len(mylist):
        if mylist[i] == value:
            return mylist

        i += 1
    return mylist


def concat(list1, list2):
    '''
    function - function to return a new list, which is a combination of list1 and list2
    :param list1: - list
    :param list2: - list
    :return:
    '''
    i = 0
    list = [list1, list2]
    con = " ".join(list)
    while i < len(list1 + list2):
        print(con)
        break


def remove(mylist, value):
    '''

    :param mylist:
    :param value:
    :return:
    '''
    i = 0
    mylist = list(mylist)
    while i < len(mylist):
        if mylist[i] == value:
            del(mylist[i])
            break
        i += 1
    return ''.join(mylist)

