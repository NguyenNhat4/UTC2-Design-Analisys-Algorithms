def lexicographic_permutations(arr):
    def next_permutation():
        i = len(arr) - 1
        while i > 0 and arr[i - 1] >= arr[i]:
            i -= 1
        if i <= 0:
            return False

        j = len(arr) - 1
        while arr[j] <= arr[i - 1]:
            j -= 1
        arr[i - 1], arr[j] = arr[j], arr[i - 1]

        arr[i:] = arr[len(arr) - 1: i - 1: -1]
        return True

    arr.sort()
    print(' '.join(str(i) for i in arr))
    while next_permutation():
        print(' '.join(str(i) for i in arr))

lexicographic_permutations([1, 2, 3, 4])
