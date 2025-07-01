from bisect import *
import sys
from collections import *
from functools import *
from heapq import *
from queue import *
from itertools import *
from math import *
from operator import *
from types import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
print = lambda *a, sep=" ", end="\n": sys.stdout.write(sep.join(map(str, a)) + end)
debug = lambda *a: sys.stderr.write(" ".join(map(str, a)) + "\n")

MOD = (10 ** 9) + 7


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


def prefixSum(arr):
    n = len(arr)
    if (n == 0):
        return []
    ps = [0] * n
    ps[0] = arr[0]
    for i in range(1, n):
        ps[i] = arr[i] + ps[i - 1]
    return ps


def suffixSum(arr):
    n = len(arr)
    if (n == 0):
        return []
    ss = [0] * n
    ss[-1] = arr[-1]
    for i in range(n - 2, -1, -1):
        ss[i] = arr[i] + ss[i + 1]
    return ss


def factors(n):
    return set(x for tup in ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0) for x in tup)


def sumDigits(no):
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))


def inde(arr):
    ind = {}
    for i in range(len(arr)):
        ind[arr[i]] = i
    return ind


def freq(arr):
    d = {}
    for i in arr:
        if (i in d):
            d[i] += 1
        else:
            d[i] = 1
    return d


def isPrime(num):
    if (num > 1):
        for i in range(2, int(sqrt(num)) + 1):
            if (num % i == 0):
                return False
        return True
    else:
        return False


def cbrt(num):
    return pow(num, 1 / 3)


def isSorted(arr):
    is_sorted = all(a <= b for a, b in zip(arr, arr[1:]))
    return is_sorted


def gcdArray(nums):
    if (len(nums) == 1):
        return nums[0]

    div = gcd(nums[0], nums[1])
    if (len(nums) == 2):
        return div
    for i in range(1, len(nums) - 1):
        div = gcd(div, nums[i + 1])
        if (div == 1):
            return div
    return div


alpha = 'abcdefghijklmnopqrstuvwxyz'


def set_bit(x, i):
    return x | (1 << i)


def clear_bit(x, i):
    return x & ~(1 << i)


def get_bit(x, i):
    return (x >> i) & 1


def dist(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    return sqrt(pow(x, 2) + pow(y, 2))


class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


def solve1(arr, d):
    t = [i + 1 for i in arr]
    for i in range(1, min(m, d + 1)):
        t[i] += 1
    tre = SegmentTree(t, default=10e9, func=min)
    for i in range(d + 1, m):
        x = tre.query(i - d - 1, i)
        tre[i] += x
    return tre[m - 1]


for _ in range(int(input())):
    n, m, k, d = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    res = []
    for i in arr:
        res.append(solve1(i, d))
    pr = [0] + prefixSum(res)
    ans = 949078567670
    for i in range(k, n + 1):
        ans = min(ans, pr[i] - pr[i - k])
    print(ans)