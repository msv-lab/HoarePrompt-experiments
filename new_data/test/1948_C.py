def sol(L, n):
    d = {}

    def helper(i, j):
        try:
            if i < 0 or i > 1 or j < 0 or j >= n:
                return False
            if i == 0 and j == 0:
                return True
            if (i == 0 and j % 2 != 0) or (i == 1 and j % 2 == 0):
                return False
            if (i, j) in d:
                return d[(i, j)]

            y = False
            if j > 0 and L[i][j - 1] == '>':
                y = (j >= 2 and helper(i, j - 2)) or helper(i - 1, j - 1) or helper(i + 1, j - 1)

            d[(i, j)] = y
            return y
        except IndexError as e:
            print(f"IndexError: i={i}, j={j}, error={e}")
            return False
        except Exception as e:
            print(f"Error: i={i}, j={j}, error={e}")
            return False

    z = helper(1, n - 1)
    if z:
        print('YES')
    else:
        print('NO')


t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input().strip()
    s2 = input().strip()
    L1 = list(s1)
    L2 = list(s2)
    L = [L1, L2]
    sol(L, n)
