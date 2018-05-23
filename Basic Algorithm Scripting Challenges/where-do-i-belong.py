#Return the lowest index at which a value (second argument) should be inserted into an array (first argument) once it has been sorted. The returned value should be a number.

def get_index_to_insert(l, n):
    l.append(n)
    l.sort()
    return l.index(n)



print(get_index_to_insert([10, 20, 30, 40, 50], 35))
print(get_index_to_insert([10, 20, 30, 40, 50], 30))
print(get_index_to_insert([40, 60], 50))
print(get_index_to_insert([3, 10, 5], 3))
print(get_index_to_insert([5, 3, 20, 3], 5))
print(get_index_to_insert([2, 20, 10], 19))
print(get_index_to_insert([2, 5, 10], 15))
