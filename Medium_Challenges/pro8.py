def insertion_sort_count(numbers):
    sorted_numbers = numbers.copy()
    number_of_shifts = 0
    for each_index in range(1, len(sorted_numbers)):
        key = sorted_numbers[each_index]
        j = each_index - 1  #check item immediately left of key

        while j >= 0 and sorted_numbers[j] > key:            #keeps going left while the index is valid and the earlier number is bigger than the key
            sorted_numbers[j + 1] = sorted_numbers[j]  #to shift that bigger number 1 position right
            number_of_shifts += 1
            j -= 1     #moves 1 position left to check nxt number
        sorted_numbers[j + 1] = key      #inserts saved key into gap left by shifts
    return sorted_numbers, number_of_shifts

print(insertion_sort_count([5, 3, 4]))
