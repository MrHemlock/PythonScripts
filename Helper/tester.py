mylist = [2, 4, 6, 7, 14, 90]


def sum_this_list(numlist):
    total = 0
    i = 0
    while i < len(numlist):
        total += numlist[i]
        i += 1
    return total


print(sum_this_list(mylist))