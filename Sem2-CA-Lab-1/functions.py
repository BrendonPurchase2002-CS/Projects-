# ScriptName: functions.py
# Author: Brendon Purchase
# Student Number: 119473576
# template for calling functions in another file


def a_function():
    return ("I'm in another file :)")


# 1
def fractions(DNA):
    try:
        dna_dict = {"C": 0, "G": 0, "T": 0, "A": 0}
        for val in DNA:
            if val == "C":
                dna_dict["C"] += 1
            elif val == "G":
                dna_dict["G"] += 1
            elif val == "T":
                dna_dict["T"] += 1
            elif val == "A":
                dna_dict["A"] += 1

        all = dna_dict["C"] + dna_dict["G"] + dna_dict["T"] + dna_dict["A"]
        values = (dna_dict["C"] / all, dna_dict["G"] / all, dna_dict["T"] / all, dna_dict["A"] / all)
        return values
    except TypeError:
        return "Input must be a string character"


print(fractions("TTACACTTAT"))

# 2
'''
def F(S1, S2):
    R = []
    for e1 in S1:
        for e2 in S2:
            if e1 == e2:
                R += [e1]
                break
    return R


print(F("12", "32"))

'''


# A


def F_while(S1, S2):
    R = []
    i = 0
    while i < len(S1):
        j = 0
        while j < len(S2):
            if S2[j] == S1[i]:
                R.append(S1[i])
            j += 1
        i += 1

    return R


# print(F_while("12", "32"))


# B


def F_list_comp(S1, S2):
    R = [e1 for e1 in S1 for e2 in S2 if e1 == e2]

    return R


# print(F_list_comp("23", "234"))


# C


def F_lambda(S1, S2):
    R = []

    return R


# D

def F_error(S1, S2):
    R = []
    try:
        for e1 in S1:
            for e2 in S2:
                if e1 == e2:
                    R += [e1]
        return R
    except:
        return 'Error!'


# 3
def frequencies(s):
    freq_dict = {}
    try:
        for i in s:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        return freq_dict
    except TypeError as t:
        t = "input is incorrect"
        return t


# print(frequencies('21'))


# 4

def firsts(s):
    inc = 0
    first_str = ""
    for i in range(len(s)):
        if first_str == "":
            first_str += s[i]
        elif s[i] not in first_str:
            first_str += s[i]

    return first_str


# print(firsts("asdfghjklasdfg"))


# 5

def extract(text, n, m):
    extract_text = ""

    return extract_text
