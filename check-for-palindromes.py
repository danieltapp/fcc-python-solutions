#UNSOLVED - LOOK INTO REGEX TO REMOVE NON-ALPHANUMERIC FROM STRING

#Return true if the given string is a palindrome. Otherwise, return false.

def palindrome(str):
    return str.lower() == ''.join(reversed(list(str))).lower()

print(palindrome('eye'))
print(palindrome('_eye'))
print(palindrome('race car'))
print(palindrome('not a palindrome'))
print(palindrome('never odd or even'))
print(palindrome('nope'))
print(palindrome('almostomla'))
print(palindrome('My age is 0, 0 si ega ym.'))
print(palindrome('1 eye for of 1 eye.'))
print(palindrome('0_0 (: /-\ :) 0-0'))
print(palindrome('five|\_/|four'))
