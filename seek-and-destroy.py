#You will be provided with an initial array (the first argument in the destroyer function), followed by one or more arguments. Remove all elements from the initial array that are of the same value as these arguments.

def destroyer(l, *args):
    return [x for x in l if x not in args]

print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))
print(destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3))
print(destroyer([3, 5, 1, 2, 2], 2, 3, 5))
print(destroyer([2, 3, 2, 3], 2, 3))
print(destroyer(["tree", "hamburger", 53], "tree", 53))
