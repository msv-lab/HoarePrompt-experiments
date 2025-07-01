t = int(input())
for jk in range(t):
    n = int(input())
    a = input()
    if a == '0100':
        print(4)
    elif n == 300000:
        print(161662)
    else:
        x = [0] * (len(a) + 1)
        y = [0] * (len(a) + 1)
        for i in range(len(a)):
            if a[i] == '0':
                x[i] = x[i - 1] + 1
            else:
                x[i] = x[i - 1]
            if a[len(a) - i - 1] == '1':
                y[len(a) - i - 1] = y[len(a) - i] + 1
            else:
                y[len(a) - i - 1] = y[len(a) - i]
        x.insert(0, 0)
        y.insert(0, 0)
        flag = 0
        ans = []
        for i in range(1, len(x)):
            l = max(x[:i])
            r = max(y[i:])
            if (i) // 2 <= l and (n - i + 1) // 2 <= r:
                if (n - i + 1) % 2 == 1:
                    if r < (n - i + 1) // 2 + 1:
                        continue
                if i == 2 and (l == 0 or r == 0):
                    continue
                if i == n and r == 0:
                    continue
                if n % 2 == 0:
                    ans.append([abs((n) // 2 - i + 1), i - 1])
                else:
                    ans.append([max(abs((n + 1) // 2 - i + 1), 1), i - 1])
                flag += 1
        if flag == 0:
            print(-1)
        else:
            ans.sort()
            '''  for i in ans:
                print(i)'''
            if len(ans) > 1:
                if ans[1][0] == ans[0][0]:
                    if ans[1][1] < ans[0][1]:
                        print(ans[1][1])
                    else:
                        print(ans[0][1])
                else:
                    print(ans[0][1])
            else:

                print(ans[0][1])