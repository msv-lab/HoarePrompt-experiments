from collections import Counter
from math import comb


def count_triangles(n, arr):
    if len(arr) >= 3:
        arr.sort()
        cum_sum = 0
        total = 0
        d = Counter(arr)
        d = {k: v for k, v in sorted(d.items(), key=lambda x: x[0])}
        ans = 0  # Define ans variable
        for i in d.keys():
            if d[i] >= 3:
                ans += comb(d[i], 3)
                ans += comb(d[i], 2) * cum_sum
                cum_sum += d[i]

            elif d[i] == 2:
                ans += comb(d[i], 2) * cum_sum
                cum_sum += d[i]
            else:
                cum_sum += d[i]
        return ans  # Add return statement
    else:
        return 0


def main():
    t = int(input())  # Define t
    while t > 0:
        n = int(input())
        sides = list(map(str, input().split()))  # Fix typo here
        result = count_triangles(n, sides)
        print(result)
        t -= 1


if __name__ == "__main__":
    main()
