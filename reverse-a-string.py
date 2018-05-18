#Reverse the provided string.

#You may need to turn the string into an array before you can reverse it.
#Your result must be a string.


def reverse_string(str):
    return ''.join(list(reversed(str)))

print(reverse_string('hello'))
print(reverse_string('Howdy'))
print(reverse_string('Greetings from Earth'))

