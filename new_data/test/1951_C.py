t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    k_cpy = k

    a_original = a

    a.sort()
    dic = {}
    fac = 0

    for ele in a:
        # if ele in dic:
        #    fac+=1
        #    ele=ele+dic[ele]*fac
        # else:
        #    fac=0
        if k >= m:
            dic[ele] = m
            k = k - m
        else:
            dic[ele] = k
            k = k - k
        if k == 0:
            break

    x, price = 0, 0
    for elem in a_original:
        if x >= k_cpy:
            break
        if elem not in dic:
            continue
        else:
            val = elem + x
            x += dic[elem]

            mapvalue = dic[elem]
            price += val * mapvalue

    print(price)