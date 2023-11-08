def binary_search(sorted_arr, target):
    # Search for a target element in a sorted array using binary search
    left, right = 0, len(sorted_arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if sorted_arr[mid] == target:
            # If the middle element is the target, return its index
            return mid
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Target not found
    return -1
