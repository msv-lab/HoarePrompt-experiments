for _ in range(int(input())):
    x = int(input())
    a = input()
    b = input()
    a = list(a)
    b = list(b)
    count = a.count('1')
    countb = b.count('1')
    ans = 0
    flag = 0
    final_ans = 0
    if count != countb:
        ans = abs(count - countb)
    for i in range(x):
        if flag >= ans:
            break
        if a[i] == "1":
            a[i] = "0"
            flag += 1
    for i in range(x):
        if a[i] == "1" and b[i] == "0":
            final_ans += 1
    print(final_ans + ans)
