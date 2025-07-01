import sys
import math

input = sys.stdin.readline


def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    s = input()
    return (list(s[:len(s) - 1]))


def invr():
    return (map(int, input().split()))


for _ in range(1):
    n = int(input())

for i in range(0, n):
    temp = inlt()
    n = temp[0]
    k = temp[1]
    health = inlt()
    pos = inlt()

    pos = [abs(0 - x) for x in pos]
    combined = zip(pos, health)
    s = sorted(combined)
    sortedlist = []
    for t in range(0, len(s)):
        currHealth = s[t][1]
        currPos = s[t][0]
        if (t > 0 and s[t][0] == s[t - 1][0]):
            sortedlist[-1] = (currPos, sortedlist[-1][1] + currHealth)
        else:
            sortedlist.append((currPos, currHealth))
    extra = 0
    ans = True
    iter = 0
    for item in sortedlist:
        curr = (k * (item[0] - iter)) + extra
        if (curr < item[1]):
            ans = False
            break
        else:
            iter = iter + (item[1] - extra) / k
            extra = extra + (curr - item[1])
    if (ans):
        print("Yes")
    else:
        print("No")
