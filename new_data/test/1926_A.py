# String of length 5
# Characters are either A or B
# Which letter shows up most frequently?

def charCount(userString):
    list(userString)
    countA = 0
    countB = 0
    for letter in userString:
        if letter == 'A':
            countA += 1
        elif letter == 'B':
            countB += 1
        else:
            continue
    if countA > countB:
        print("A")
    elif countB > countA:
        print("B")
    else:
        pass


userStrings = ["8", "ABABB", "ABABA", "BBBAB", "AAAAA", "BBBBB", "BABAA", "AAAAB", "BAAAA"]

for userString in userStrings:
    charCount(userString)
