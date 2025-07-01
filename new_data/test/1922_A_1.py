def solve(a, b, c):
    for A, B, C in zip(a, b, c):
        if (A == C or B == C) and not A == B == C:
            return False
    return True


t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()
    c = input().strip()

    ans = solve(a, b, c)
    print("YES" if ans else "NO")