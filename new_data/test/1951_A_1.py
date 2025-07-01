t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    count_ones = s.count('1')

    if count_ones % 2 == 1:
        print("NO")
    else:
        print("YES")
