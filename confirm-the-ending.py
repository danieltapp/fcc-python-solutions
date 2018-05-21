#Check if a string (first argument, str) ends with the given target string (second argument, target).

def confirm_ending(str, x):
    return str.endswith(x)


print(confirm_ending("Bastian", "n"))
print(confirm_ending("Connor", "n"))
print(confirm_ending("Walking on water and developing software from a specification are easy if both are frozen", "specification"))
print(confirm_ending("Open sesame", "same"))
print(confirm_ending("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain"))


