def left_rotation(array, n):
    return array[n:] + array[:n]

print(left_rotation([1, 2, 3, 4, 5], 2))
