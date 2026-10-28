def most_frequent(numbers):
    if numbers == []:
        return None

    frequency = {}
    for each_number in numbers:
        if each_number in frequency:
            frequency[each_number] += 1
        else:
            frequency[each_number] = 1
    most_common_number = numbers[0]
    highest_count = frequency[most_common_number]

    for each_number in numbers:
        if frequency[each_number] > highest_count:
            most_common_number = each_number
            highest_count = frequency[most_common_number]
    return most_common_number

print(most_frequent([2, 5, 2, 8, 2, 5]))
print(most_frequent([4, 7, 7, 4]))
print(most_frequent([]))