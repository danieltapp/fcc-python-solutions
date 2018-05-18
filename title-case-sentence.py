#UNSOLVED - LOOK INTO REGEX TO REMOVE NON-ALPHANUMERIC FROM STRING

#Return the provided string with the first letter of each word capitalized. Make sure the rest of the word is in lower case.

def title_case(str):
    return str.lower().title()
   

print(title_case("I'm a little tea pot"))
print(title_case('sHoRt AnD sToUt'))
print(title_case('HERE IS MY HANDLE HERE IS MY SPOUT'))
print(title_case('fart knocker'))
