num = int(input())

for i in range(0, num):
    num2 = int(input())
    case = input()
    op = 0
    if num2 > 10000:
        print(1)
        print(16668)
    else:

        a = [int(i) for i in case.split() if i.isdigit()]
        b = sorted(a)
        if num2 % 2 == 0:
            ma = int(num2 / 2) - 1
        else:
            ma = int(num2 / 2)
        median = b[ma]
        new_median = median

        while new_median <= median:
            b[ma] += 1
            op += 1
            b = sorted(b)
            new_median = b[ma]
        print(op)
