def binary_search(sorted_array, target):
    low = 0
    high = len(sorted_array) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        mid_value = sorted_array[mid]

        iterations += 1

        if mid_value < target:
            low = mid + 1
        elif mid_value > target:
            high = mid - 1
        else:
            return iterations, mid_value
    if low < len(sorted_array):
        upper_bound = sorted_array[low]
    else:
        upper_bound = None

    return iterations, upper_bound


print(binary_search([1.2, 1.2, 1.3, 1.6, 2.0, 3.0], 1.3))
