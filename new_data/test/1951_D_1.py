import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        if k > n:
            print("NO")
            continue
        if k == 0:
            print("NO")
            continue
        if k == n:
            print("YES")
            print(1)
            print(1)
            continue
        if k == 1:
            print("YES")
            print(1)
            print(n)
            continue
        if k <= 60:
            p = []
            remaining = n
            sum_q = 0
            possible = True
            for i in range(k):
                if remaining <= 0:
                    break
                p_i = (remaining + 1) // 2
                q_i = remaining // p_i
                sum_q += q_i
                if sum_q > k:
                    possible = False
                    break
                p.append(p_i)
                remaining = remaining % p_i
            if possible and sum_q == k:
                print("YES")
                print(len(p))
                print(' '.join(map(str, p)))
            else:
                found = False
                low = (n // (k + 1)) + 1
                high = n // k
                if low <= high:
                    p_candidate = high
                    if p_candidate > 0 and (n // p_candidate) == k:
                        print("YES")
                        print(1)
                        print(p_candidate)
                        found = True
                if not found:
                    print("NO")
        else:
            low = (n // (k + 1)) + 1
            high = n // k
            if low > high:
                print("NO")
            else:
                p_candidate = high
                if p_candidate <= 0:
                    print("NO")
                    continue
                q_candidate = n // p_candidate
                if q_candidate == k:
                    print("YES")
                    print(1)
                    print(p_candidate)
                else:
                    print("NO")

if __name__ == "__main__":
    solve()
