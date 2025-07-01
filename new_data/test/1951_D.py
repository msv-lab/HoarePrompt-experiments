def solve():
    import sys
    input = sys.stdin.read().split()
    t = int(input[0])
    ptr = 1
    for _ in range(t):
        n = int(input[ptr])
        k = int(input[ptr+1])
        ptr += 2
        if k == 1:
            print("YES")
            print(1)
            print(n)
            continue
        bit_count = bin(n).count('1')
        if k > bit_count:
            if n >= k:
                x = n - k + 1
                if x <= n // 2:
                    print("NO")
                else:
                    print("YES")
                    print(2)
                    print(x, 1)
            else:
                print("NO")
        else:
            bits = []
            for i in reversed(range(n.bit_length())):
                if (n >> i) & 1:
                    bits.append(i)
            mer = bit_count - k + 1
            fir = 0
            for i in range(mer):
                fir += (1 << bits[i])
            ans = [fir] + [(1 << b) for b in bits[mer:]]
            print("YES")
            print(len(ans))
            print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()