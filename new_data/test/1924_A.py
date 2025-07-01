
import sys
from itertools import product

def is_subsequence(t, s):
    it = iter(s)
    for c in t:
        flag = False
        for sc in it:
            if sc == c:
                flag = True
                break
        if not flag:
            return False
    return True

def main():
    input = sys.stdin.read().split()
    t = int(input[0])
    ptr = 1
    for _ in range(t):
        n = int(input[ptr])
        k = int(input[ptr+1])
        m = int(input[ptr+2])
        s = input[ptr+3]
        ptr +=4
        # Step 1: Count character frequencies
        counts = [0] * k
        for c in s:
            if 'a' <= c <= chr(ord('a') + k -1):
                counts[ord(c) - ord('a')] +=1
        # Check if any character count is less than n
        missing = ""
        for i in range(k):
            if counts[i] < n:
                missing = chr(ord('a') + i) * n
                break
        if missing:
            print("NO")
            print(missing)
            continue
        # Step 2: If k^n <= 100, check all combinations
        if k**n <=100:
            letters = [chr(ord('a') + i) for i in range(k)]
            for comb in product(letters, repeat=n):
                t_str = ''.join(comb)
                if not is_subsequence(t_str, s):
                    print("NO")
                    print(t_str)
                    break
            else:
                print("YES")
        else:
            print("YES")

if __name__ == '__main__':
    main()
