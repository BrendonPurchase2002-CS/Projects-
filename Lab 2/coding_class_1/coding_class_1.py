# author: Brendon Purchase
# Student Number: 119473576


def all_pairs(s1, s2):
    """

    :param s1: = list/string
    :param s2: = list/string
    :return: = a list with all pairs of elements from list s1 and s2 respectively, with the second element varying more
     rapidly than the first
    """

    combo = []

    i = 0
    j = 0
    while i < len(s1):
        while j < len(s2):
            combo.append(str(s1[i]) + str(s2[j]))

            j += 1

        i += 1
        return False, combo


print(all_pairs([1, 2], "abc"))
