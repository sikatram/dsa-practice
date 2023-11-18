class Algorithm:
    def binary_search(sorted_arr, target):
        left = 0
        right = len(sorted_arr)

        while left < right:
            mid = (left + right) // 2
            if target == sorted_arr[mid]:
                return True
            elif target < sorted_arr[mid]:
                right = mid
            else:
                left = mid + 1

        return False
