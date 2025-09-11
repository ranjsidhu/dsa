# list1 and list2 must be sorted


def merge(list1, list2):
    combined = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


first_list = [1, 2, 7, 8]
second_list = [3, 4, 5, 6]
print(merge(first_list, second_list))

unsorted_list = [3, 1, 4, 2]


def merge_sort(arr):
    if (len(arr)) == 1:
        return arr
    mid_index = int(len(arr) / 2)
    left = merge_sort(arr[:mid_index])
    right = merge_sort(arr[mid_index:])

    return merge(left, right)


print(merge_sort(unsorted_list))
