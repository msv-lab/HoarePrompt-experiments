def position_wins(
        n,  # number of cows
        k,  # cow position
        v  # cow value
):
    curr_wins = 0
    if k > 0 and k < n - 1:
        curr_wins += 1 if a[k - 1] < v else 0
        curr_wins += 1 if a[k + 1] < v else 0
    elif k == 0:
        curr_wins += 1 if a[k + 1] < v else 0
    elif k == n:
        curr_wins += 1 if a[k - 1] < v else 0
    return curr_wins


t = int(input())

for _ in range(t):
    test_case = input().split(" ")
    n = int(test_case[0])
    k = int(test_case[1]) - 1
    a = list(map(int, input().split(" ")))

    curr_pos = 0
    wins = 0

    curr_wins = position_wins(n, k, a[k])
    greater_cows = list(filter(lambda x: x > a[k], a))
    pos_first_g_c = a.index(greater_cows[0]) if greater_cows else n - 1
    g_n_wins = position_wins(n, pos_first_g_c, a[k]) if pos_first_g_c < k else 0
    candidate_cows_curr = list(filter(lambda x: a.index(x) < pos_first_g_c, a))

    a[pos_first_g_c], a[k] = a[k], a[pos_first_g_c]
    greater_cows = list(filter(lambda x: x > a[pos_first_g_c], a))
    before_pos_first_g_c = pos_first_g_c
    pos_first_g_c = a.index(greater_cows[0]) if greater_cows else n - 1
    candidate_cows_with_change = list(
        filter(lambda x: a.index(x) < pos_first_g_c and a.index(x) > before_pos_first_g_c, a))

    change_pos_wins = (len(candidate_cows_with_change) or 1) + g_n_wins - 1
    curr_pos_wins = (len(candidate_cows_curr) or 1) - 1 + (curr_wins - 1)
    wins = max(curr_pos_wins, change_pos_wins, curr_wins, g_n_wins)

    print(wins)