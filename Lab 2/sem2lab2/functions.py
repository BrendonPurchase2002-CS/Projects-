# ScriptName: functions.py
# Author: Jason Quinlan

# template for calling functions in another file


def a_function():
    return "I'm in another file :)"


# q1
powers = [i for i in range(1, 6) if i % 2 == 0]

# q2
'''def EF(s1, s2):
    r = []
    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
                r += [e1]
                break
    return r
'''


def F(s1, s2):
    r = []
    i = 0

    while i < len(s1):
        j = 0
        while j < len(s2):
            if s1[i] == s2[j]:
                r.append(s1[i])
            j += 1
        i += 1
    return r


# print(F([1, 2, 3], [1, 4, 3]))


# q3
# A

# d = {"119346876": ["CS1117", "CS1116"], "119345890": ["CS1119", "CS1110"], "119234567": ["CS1119", "CS1111", "CS1110"],
# "119876234": ["CS1115", "CS1119"]}


def reducedFeeEntitlement(d):
    fee = []
    for val in d:
        if len(d[val]) <= 2:
            fee.append(val)
    return fee


#print(reducedFeeEntitlement(d={"119346876": ["CS1117", "CS1116"], "119345890": ["CS1119", "CS1110"],
                        #       "119234567": ["CS1119", "CS1111", "CS1110"], "119876234": ["CS1115", "CS1119"]}))


# B


def commonModules(d, s1, s2):
    r = []

    d = {"119346876": ["CS1117", "CS1116"], "119345890": ["CS1119", "CS1110"],
         "119234567": ["CS1119", "CS1111", "CS1110"], "119876234": ["CS1115", "CS1119"]}
    first = d[s1]
    second = d[s2]
    i = 0
    while i < len(first):
        j = 0
        while j < len(second):
            if first[i] == second[j]:
                r.append(first[i])
            j += 1
        i += 1
    return r


print(commonModules({"119346876": ["CS1117", "CS1116"], "119345890": ["CS1119", "CS1110"],
                     "119234567": ["CS1119", "CS1116", "CS1110"], "119876234": ["CS1115", "CS1119"]}, "119346876",
                    "119234567"))


# q4
def iter_factorial(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    else:
        return n * iter_factorial(n - 1)


# q5

def Fizbuzz(val):
    for val in range(1, 100):
        if val % 3 == 0 and val % 4 == 0:
            print("FizzBuzz")
        elif val % 3 == 0:
            print("Fizz")
        elif val % 4 == 0:
            print("Buzz")


#Fizbuzz(val=100)
