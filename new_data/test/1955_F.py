import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b, c, d = map(int, sys.stdin.readline().split())
        # Calculate parities of each count
        p1 = a % 2
        p2 = b % 2
        p3 = c % 2
        p4 = d % 2
        # Compute the initial XOR based on parities
        initial_xor = p1 * 1 ^ p2 * 2 ^ p3 * 3 ^ p4 * 4
        # Calculate sum of floor division by 2 for each count
        s = (a // 2) + (b // 2) + (c // 2) + (d // 2)
        # Determine the answer based on initial XOR and s
        if initial_xor == 0:
            if s == 0:
                print(1)
            else:
                print(s)
        else:
            print(s)

if __name__ == "__main__":
    main()