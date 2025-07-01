from sys import stdin, stdout

p = stdout.write
# ---------COLLECTIONS--------#
from collections import defaultdict as maps
# using this, we can give a default value of data type to dict
from collections import OrderedDict
# this stores the order of insertion of values in dict
from collections import Counter as freq
# returns a dict containing count of values
from collections import ChainMap


# to have diff. dicts in one class (container)
# we have to use .new_child(new_dictToInsert) to insert a new dict into ChainMap
# -------COLLECTIONS---------- #

def getlist():
    return list(map(int, stdin.readline().split()))


def getinp():
    return map(int, stdin.readline().split())


def getstr():
    return stdin.readline().rstrip()


def getnum():
    return int(stdin.readline())


# -----------MAIN CODE----------#
def main():
    for _ in range(int(stdin.readline())):
        n, k = getinp()
        r = ""
        for i in range(k):
            r += chr(97 + i)
        if n <= 3:
            p(r * n + "\n")
        else:
            p(r * (n - 1) + 'a' + "\n")


# -----------MAIN CODE-----------#
if __name__ == "__main__":
    main()