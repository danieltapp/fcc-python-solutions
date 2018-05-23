#One of the simplest and most widely known ciphers is a Caesar cipher, also known as a shift cipher. In a shift cipher the meanings of the letters are shifted by some set amount.

#A common modern use is the ROT13 cipher, where the values of the letters are shifted by 13 places. Thus 'A' ↔ 'N', 'B' ↔ 'O' and so on.

#Write a function which takes a ROT13 encoded string as input and returns a decoded string.

def rot13(str):
    l = list(str.lower())
    for i in range(0, len(l)):
        if l[i].isalpha():
            if ord(l[i]) > 109:
                l[i] = chr(ord(l[i]) - 13)
            elif ord(l[i]) <= 109:
                l[i] = chr(ord(l[i]) + 13)
    return ''.join(l).upper()


print(rot13("SERR PBQR PNZC"))
print(rot13('SERR CVMMN!'))
print(rot13("SERR YBIR?"))
print(rot13("GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK."))
