'''def peaks(numlist):
    melist = []
    i = 0
    while i < len(numlist):
        if i == 0:
            melist.append(numlist[i])
            i += 1
            continue

        if numlist[i] < numlist[i]:
            melist.append(numlist[i])
        i += 1

    return False, melist


print(peaks([3, 2, 5, 5, 7, 6, 1, 8, 4]))

'''

def peaks(numlist):
    try:
        if not numlist:
            return False, []
        i = 0
        melist = []
        melist += [numlist[i]]
        for index in numlist:
            if index > melist[i]:
                melist += [index]
                i += 1

        return False, melist
    except:
        return True, -1


print(peaks([3, 2, 5, 5, 7, 6, 1, 8, 4]))
