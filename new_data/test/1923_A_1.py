'''

0 과 1로 이루어진 배열을 받고 난 후
0으로만 연속되고 1으로만 연속된 하나의 블록으로 만드는 것이 목표임
오른쪽에 있는 1을 가장 가까운 왼쪽으로 옮겨서 독립된 0, 1 블록으로 만들어야 함

그냥 중간에 비어있는 0의 갯수가 정답일 듯

'''

t = int(input())

for _ in range(t):
    length = int(input())
    arrs = list(map(int, input().split()))

    cnt0 = 0

    for idx in range(len(arrs)):
        if arrs[0] == 0 and idx != 0:  # 0이면 0으로 이루어지다가 1로 이루어져야함
            if arrs[idx] == 0:
                cnt0 += 1
        elif arrs[0] == 1:  # 처음이 1이면 무조건 0
            if arrs[idx] == 0:
                cnt0 += 1

    cnt1 = 0

    for idx in range(len(arrs)):
        if arrs[idx] == 1:
            cnt1 += 1

    if arrs[0] == 0:
        if arrs[len(arrs) - 1] == 0:
            cnt0 -= 1

    ans = 0

    if cnt1 == 1 or cnt1 == 0:
        ans = 0
    else:
        ans = cnt0

    print(ans)