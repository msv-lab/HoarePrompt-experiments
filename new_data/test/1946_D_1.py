import sys


def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, x = int(input[ptr]), int(input[ptr + 1])
        ptr += 2
        a = list(map(int, input[ptr:ptr + n]))
        ptr += n

        current_or = 0
        current_xor = 0
        k = 0
        for num in a:
            current_xor ^= num
            if (current_or | current_xor) <= x:
                k += 1
                current_or |= current_xor
                current_xor = 0

        if current_xor == 0 and k >= 1:
            print(k)
        else:
            # Check if the entire array's XOR is <=x
            total_xor = 0
            for num in a:
                total_xor ^= num
            if total_xor <= x:
                print(1)
            else:
                print(-1)


if __name__ == "__main__":
    main()