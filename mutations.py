#Return true if the string in the first element of the array contains all of the letters of the string in the second element of the array.

def mutation(l):
    a = list(l[0].lower())
    b = list(l[1].lower())
    x = 0
    for i in range(0, len(b)):
        if b[i] in a:
            x += 1
        else:
            return False
    return True



print(mutation(["hello", "hey"]))
print(mutation(["hello", "Hello"]))
print(mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]))
print(mutation(["Mary", "Army"]))
print(mutation(["Mary", "Aarmy"]))
print(mutation(["Alien", "line"]))
print(mutation(["floor", "for"]))
print(mutation(["hello", "neo"]))
print(mutation(["voodoo", "no"]))

