"""
The first list is [1,3,5]
The second list is [2,4,5]

Determine whether the lists have an item in common
"""

list_1 = [1, 3, 5]
list_2 = [2, 4, 5]


def naive_item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True

    return False


def item_in_common(list_1, list_2):
    dict_found = {}
    for i in list_1:
        dict_found[i] = True

    for j in list_2:
        if j in dict_found:
            return True

    return False


print(naive_item_in_common(list_1, list_2))
print(item_in_common(list_1, list_2))
