    if low == high:
        return arr[low]

    mid = (low + high) // 2
    max_left = find_max(arr, low, mid)
    max_right = find_max(arr, mid + 1, high)

    return max(max_left, max_right)


b = [1,3,4,5,6,7,8,9]


print(find_max(b, 0, len(b)))


