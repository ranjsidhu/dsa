unsorted_list = [4, 2, 6, 5, 1, 3]


def insertion_sort(arr):

    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        while temp < arr[j] and j > -1:
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1

    return arr


print(insertion_sort(unsorted_list))
