import math
import re


def input_n(isOne=False):
    if not isOne:
        return int(input())
    else:
        return 1


def input_list(space=True, to_int=True):
    line = input()
    if space:
        items = line.split()
    else:
        items = list(line)

    if to_int:
        return [int(i) for i in items]
    else:
        return items


def list_to_string(arr, sym):
    string = ""
    for i in arr:
        string += str(i) + sym
    return string


def find_all_indices_string(string, substring):
    indices = []
    index = string.find(substring)
    while index != -1:
        indices.append(index)
        index = string.find(substring, index + 1)
    return indices


def find_all_indices_arr(arr, element):
    return [index for index, value in enumerate(arr) if value == element]


def find_arr_in_arr(arr, index, value):
    for subArray in arr:
        if subArray[index] == value:
            return subArray
    return None


def solve():
    n = int(input())
    start = -1
    end = 1e9
    num = []
    for i in range(n):
        t, v = tuple(map(int, input().split()))
        if t == 1:
            if start < v: start = v
        if t == 2:
            if end > v: end = v
        if t == 3: num.append(v)
    count_num = 0
    for i in num:
        if i < start or i > end:
            continue
        else:
            count_num += 1
    if start > end: return 0
    return end - start + 1 - count_num if end - start + 1 >= count_num else 0


n = input_n()
ans = []
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(n):
    ans.append(solve())
for i in ans:
    print(i)
