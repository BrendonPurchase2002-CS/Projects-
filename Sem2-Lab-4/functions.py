# ScriptName: functions.py
# Author: Jason Quinlan

# template for calling functions in another file


def a_function():
    return ("I'm in another file :)")


# 1
def chooseLargest(a, b):
    result = []
    #
    #     result.append(list(map(max, a, b)))
    #     print(result)
    #
    #
    # l1 = [1, 2, 3, 4, 5]
    # l2 = [2, 2, 9, 0, 9]
    # chooseLargest(l1, l2)

    for i in zip(a, b):
        result.append(list(map(max, [i[1]], [i[0]])))

    return result


l1 = [1, 2, 3, 4, 5]
l2 = [2, 2, 9, 0, 9]


# print(chooseLargest(l1, l2))


# 2


def read_draw():
    lst = []

    infile = open("lotteryNumbers.txt", "r")
    info = infile.readlines()
    for i in info:
        temp_lst = []
        for num in i[0:-1].split():
            temp_lst.append(int(num))
        if len(temp_lst) > 0:
            lst.append(temp_lst)
    return lst


print(read_draw())


# 3

def del_1000(courierData):
    return


def most_del(courierData):
    return


# 4


def append_list():
    list1 = [1, 2, 3]
    list2 = [10, 20, 30]
    totals = []
    for tup in zip(list1, list2):
        totals.append(list(map(lambda d, e: d + e, [tup[1]], [tup[0]])))

    return totals


# print(append_list())


# 5
def client_matcher():
    infile = open("clients.txt", "r")
    info = infile.readlines()  
    print(info)


client_matcher()
