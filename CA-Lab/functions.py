# ScriptName: functions.py
# Author: Brendon Purchase
# StudentNum: 119473576

# template for calling functions in another file


def print_function():
    return "I'm in another file :)"


def to_english(n):
    nums = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
            9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
            16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
            90: 'ninety'}

    # n_hundreds = n // 100  # get the hundreds value of da thing
    # n_tens = n % 100  # get the tens value of the thing and ones value together
    # n_tenssing = n_tens // 10  # gets just the tens value of the number
    # n_ones = n_tens % 10  # gets the ones value of the number

    length = len(str(n))  # converts to string
    en = n * -1

    if n in range(1, 10):  # one to ten
        if n in nums.keys():
            return nums[n].capitalize()

    elif n in range(10, 100):  # ten to nineteen
        if n in nums.keys():
            return nums[n].capitalize()
        else:
            return nums[n // 10 * 10].capitalize() + "-" + nums[n % 10]

    elif n in range(100, 1000):
        if n % 100 == 0:
            return nums[n // 100].capitalize() + " hundred"
        else:
            return nums[n // 100].capitalize() + " hundred and " + to_english(n % 100).lower()

    elif n < 0:
        if en in nums.keys():
            return 'Minus ' + nums[en]
        elif en in range(20, 100):
            return 'Minus ' + nums[en // 10 * 10] + "-" + nums[en % 10]

        elif en % 100 == 0:
            return 'Minus ' + nums[en // 100] + " hundred"

        else:
            return 'Minus ' + nums[en // 100] + " hundred and " + to_english(en % 100)


def sort_a_list(s):
    sort_empty = []
    i = 0
    for num in range(len(s)):
        sort_empty.append(min(s))
        s.remove(min(s))
    while i <= (len(sort_empty) - 1):
        if sort_empty[i] not in s:
            s.append(sort_empty[i])
        else:
            i += 1

    return s


def ascii_difference(m, n):
    combined_list = []
    difference_list = []
    i = 0
    if len(m) > 1:
        while i < len(n):
            combined = ord(str(m[i])) + ord(str(n[i]))
            difference = ord(str(m[i])) - ord(str(n[i]))
            combined_list.append(combined)
            difference_list.append(difference * -1)

            i += 1

    if len(m) == 0:
        j = 0
        while j < len(n):
            combined = ord(str(n[j]))
            combined_list.append(combined)
            difference_list.append(combined)
            j += 1

    if len(n) == 0:
        k = 0
        while k < len(m):
            combined = ord(str(m[k]))
            combined_list.append(combined)
            difference_list.append(combined)
            k += 1
    return combined_list, difference_list




'''
              if len(m) == 0:
            combined = ord(str(n[i]))
            combined_list.append(combined)
            difference_list.append(combined)
        elif len(n) == 0:
            combined = ord(str(m[i]))
            combined_list.append(combined)
            difference_list.append(combined) 
            
            
             
    combined_list1 = []
    difference_list1 = []
    m_index_zero = str(m[0])
    m_index_one = str(m[1])
    n_index_zero = str(n[0])
    n_index_one = str(n[1])
        
    combined_list1.append(ord(m_index_zero) + ord(n_index_zero)), combined_list1.append(ord(m_index_one) + ord(n_index_one))
    difference_list1.append(abs(ord(m_index_zero) - ord(n_index_zero))), difference_list1.append(abs(ord(m_index_one) - ord(n_index_one)))

    return combined_list1, difference_list1
'''

'''
        x = list(set(sort_empty))
    return x
'''
