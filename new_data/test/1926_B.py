for _ in range(int(input())):
    n = int(input())
    l = [''] * n
    p = -1
    for i in range(n):
        l[i] = input()
        if (a := l[i].find("1")) > -1 and p == -1:
            p = i
            j = a
    k = l[p].count("1")
    m = l[p].rfind("1")
    if k > 1 and m != j:
        size = m - j + 1
        i = p + 1
        test = True
        while test and i < n:
            test = size == l[i].count('1')
            i += 1
        if test:
            print("SQUARE")
        else:
            print("TRIANGLE")
    else:
        print("TRIANGLE")
