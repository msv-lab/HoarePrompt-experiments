t = int(input())

for _ in range(t):
    n = int(input())
    cats_1 = input().strip()
    cats_2 = input().strip()

    if cats_1 == cats_2:
        print("0")
        continue

    ones1 = cats_1.count('1')
    ones2 = cats_2.count('1')

    if abs(ones1 - ones2) == n:
        print(n)
        continue

    ans = abs(ones1 - ones2)

    if ones1 < ones2:
        j = 0
        for i in range(ans):
            if cats_1[j] == '0' and cats_2[j] == '1':
                cats_1 = cats_1[:j] + '1' + cats_1[j + 1:]
                i += 1
            j += 1
    elif ones1 > ones2:
        index = 0
        for i in range(ans):
            if cats_1[index] == '1' and cats_2[index] == '0':
                cats_1 = cats_1[:index] + '0' + cats_1[index + 1:]
                i += 1
            index += 1

    if cats_1 == cats_2:
        print(ans)
        continue

    ans_2 = sum(c1 != c2 for c1, c2 in zip(cats_1, cats_2))
    print(ans + (ans_2 // 2))
