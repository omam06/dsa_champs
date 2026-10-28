def first_position(numbers, target):
    low = 0
    high = len(numbers) -1
    result = -1

    while low <= high:
        middle = (low + high) // 2
        if numbers[middle] == target:
            result = middle
            high = middle - 1
        elif numbers[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return result

print(first_position([2, 4, 4, 4, 8, 10], 4))
print(first_position([1, 3, 5, 7], 6))