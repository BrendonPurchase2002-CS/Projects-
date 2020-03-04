def chooseLargest(a, b):
    list(map(lambda tup: max(tup[0] + tup[1]), zip(a, b)))
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 2, 9, 0, 9]
    return list(map(lambda tup: max(tup[0] + tup[1]), zip(a, b)))