def min_max(nums: list[float | int]):
  if not nums:
    raise ValueError("Список не может быть пустым")
  return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]):
  return sorted(list(set(nums)))

def flatten(mat: list[list | tuple]):
  result = []
  for row in mat:
    if not isinstance(row, (list, tuple)):
      raise TypeError("Все элементы должны быть списками или кортежами")
    for item in row:
      result.append(item)
  return result

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([]))


print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2 ]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print(flatten([[1, 2,], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
