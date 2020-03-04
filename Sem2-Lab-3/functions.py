# ScriptName: functions.py
# Author: Brendon Purchase
# Student Number: 119473576

# template for calling functions in another file

hexToBinaryTable = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                    '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
                    'E': '1110', 'F': '1111'}

codon_map = {'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine',
             'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine',
             'UAC': 'Tyrosine', 'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan',
             'UAA': 'stop', 'UAG': 'stop', 'UGA': 'stop'}


def a_function():
    return ("I'm in another file :)")


# 1
def removeVowels(sentence):
    vowels = "aeiou"
    filtered_list = [l for l in sentence if l not in vowels]
    return "".join(filtered_list)


# 2
def hailStone(n):
    hail_list = []
    while n != 1:
        hail_list.append(n)

        if n % 2 == 0:
            n = n // 2
            hail_list.append(n)

            continue

        elif n % 2 != 0:
            n = (3 * n) + 1
            hail_list.append(n)

    return hail_list


# 3
def hexToBinary(hex, d):
    i = 0
    final_hex = ""
    while len(hex) > i:
        for x in hex:
            final_hex = final_hex + hexToBinaryTable.get(hex[i])

            i += 1
    return final_hex


# 4

def proteins(RNA, codon_map):
    return
