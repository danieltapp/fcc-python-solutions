#Remove all falsy values from an array.

#Falsy values in JavaScript are false, null, 0, "", undefined, and NaN.

def bouncer(l):
    return [i for i in l if i]


print(bouncer([7, "ate", "", False, 9]))
print(bouncer(["a", "b", "c"]))
print(bouncer([False, None, 0, ""]))

