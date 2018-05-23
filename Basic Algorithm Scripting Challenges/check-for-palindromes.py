#Return true if the given string is a palindrome. Otherwise, return false.

def palindrome(str):
    rev = [l.lower() for l in str if l.isalpha()]
    beg = list(reversed(rev))
    print(beg, rev)
    return ''.join(rev) == ''.join(beg)

print(palindrome('Eye'))
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
