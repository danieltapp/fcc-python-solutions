#Return the remaining elements of an array after chopping off n elements from the head.

def slasher(l,n):
    return l[n:]


print(slasher([1, 2, 3], 2))
print(slasher([1, 2, 3], 0))
print(slasher([1, 2, 3], 9))
print(slasher([1, 2, 3], 4))
print(slasher(["burgers", "fries", "shake"], 1))
print(slasher([1, 2, "chicken", 3, "potatoes", "cheese", 4], 5))
