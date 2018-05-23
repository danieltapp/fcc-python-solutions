#Write a function that splits an array (first argument) into groups the length of size (second argument) and returns them as a two-dimensional array.

def chunk_array_in_groups(list, size):
    return [list[i:i + size] for i in range(0, len(list), size)]


print(chunk_array_in_groups(["a", "b", "c", "d"], 2))
print(chunk_array_in_groups([0, 1, 2, 3, 4, 5], 3))
print(chunk_array_in_groups([0, 1, 2, 3, 4, 5], 2))
print(chunk_array_in_groups([0, 1, 2, 3, 4, 5], 4))
print(chunk_array_in_groups([0, 1, 2, 3, 4, 5, 6], 3))
print(chunk_array_in_groups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4))
print(chunk_array_in_groups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2))
