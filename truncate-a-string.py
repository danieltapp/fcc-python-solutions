#Truncate a string (first argument) if it is longer than the given maximum string length (second argument). Return the truncated string with a ... ending.

def truncate_string(str, n):
    if len(str) > n:
        if n <= 3:
            return str[:n] + '...'
        else:
            return str[:n - 3] + '...'
    else:
        return str


print(truncate_string("A-tisket a-tasket A green and yellow basket", 11))
print(truncate_string("Peter Piper picked a peck of pickled peppers", 14))
print(truncate_string("A-tisket a-tasket A green and yellow basket",len( "A-tisket a-tasket A green and yellow basket")))
print(truncate_string("A-tisket a-tasket A green and yellow basket", len( "A-tisket a-tasket A green and yellow basket") + 2))
print(truncate_string("A-", 1))
print(truncate_string("Absolutely Longer", 2))
