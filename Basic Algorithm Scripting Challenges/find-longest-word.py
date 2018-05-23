#Return the length of the longest word in the provided sentence.

#Your response should be a number.

def find_longest_word(str):
    return len(max(str.split(), key=len))
    

print(find_longest_word('The quick brown fox jumped over the lazy dog'))
print(find_longest_word('May the force be with you'))
print(find_longest_word('Google do a barrel roll'))
print(find_longest_word('What is the average airspeed velocity of an unladen swallow'))
print(find_longest_word('What if we try a super-long word such as otorhinolaryngology'))
