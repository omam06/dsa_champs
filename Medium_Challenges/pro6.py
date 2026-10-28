def closest_number(numbers, target):
    if numbers == []:
        return None
    closest = numbers[0]
    for each_number in numbers:
        dis = abs(each_number - target)
        dis2 = abs(closest - target)

        if dis < dis2:
            closest = each_number
        elif dis == dis2 and each_number < closest:
            closest = each_number
    return closest

print(closest_number([4, 8, 15, 20], 13))
print(closest_number([8, 12], 10))