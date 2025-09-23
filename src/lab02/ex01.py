def min_max (nums):
    if len(nums) == 0:
        raise ValueError("Список пуст")
    return min(nums), max(nums)


def unique_sorted(nums):
    return sorted(set(nums))


def flatten(matrix):   
    result = []
    for row in matrix:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Внутри могут быть только списки или кортежи")
        
        for item in row:
            result.append(item)
            
    return result

print("min_max ")
print(min_max([3, -1, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))

try:
    min_max([])
except ValueError:
    print("[] → ValueError")


print("\n unique_sorted ")
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, 0, -1, 2]))


print("\n flatten ")
print(flatten([[1, 2], [3, 4]]))
print(flatten( ((1, 2), (3, 4, 5)) ))
try:
    flatten([[1], "a"])
except TypeError:
    print("[[1], 'a'] → TypeError")
