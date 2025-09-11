def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


def pivot(arr, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            swap(arr, swap_index, i)

    swap(arr, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(arr, left, right):
    if left < right:
        pivot_index = pivot(arr, left, right)
        quick_sort_helper(arr, left, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, right)

    return arr


def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr) - 1)


unsorted_list = [4, 6, 1, 7, 3, 2, 5]
print(pivot(unsorted_list, 0, 6))
print(unsorted_list)
print(quick_sort(unsorted_list))
