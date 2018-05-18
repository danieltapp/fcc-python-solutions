#Return the factorial of the provided integer.
#If the integer is represented with the letter n, a factorial is the product of all positive integers less than or equal to n.
#Factorials are often represented with the shorthand notation n!
#For example: 5! = 1 * 2 * 3 * 4 * 5 = 120

def factorialize(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n -1
    return num

print(factorialize(5))
print(factorialize(10))
print(factorialize(20))
print(factorialize(0))
