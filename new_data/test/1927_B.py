def solve(n, a):
    sam = 'abcdefghijklmnopqrstuvqwxyz'
    a_map = {x: 0 for x in range(n)}
    res = ""
    for i in range(n):
        beg = a_map[a[i]]
        # print("beg = ",beg)
        res += sam[a_map[a[i]] % 27]
        a_map[a[i]] += 1
    # print(a_map)
    # print("res = ",res)
    return res


t = int(input())
for i in range(t):
    n = int(input())
    # s = input()
    # a,b,r = map(int,input().split())
    a = list(map(int, input().split()))
    # b = list(map(int,input().split()))
    ans = solve(n, a)
    print(ans)
    # print("Yes") if ans else print("No")