t = int(input())

for i in range(t):
    n = int(input())
    s = str(input())

    large_idx = []
    less_idx = []

    l_nearest_large = [0] * n
    r_nearest_less = [0] * n

    l_large_count = [0] * n
    r_less_count = [0] * n

    l_large_rank = [-1] * n
    r_less_rank = [-1] * n

    l_large_sum = [0] * n
    r_less_sum = [0] * n

    for j in range(n):
        if j == 0:
            l_large_sum[j] = 0
        else:
            l_large_sum[j] = l_large_sum[j - 1] + len(large_idx)

        if len(large_idx) > 0:
            l_nearest_large[j] = large_idx[-1]
        else:
            l_nearest_large[j] = -1

        l_large_count[j] = len(large_idx)

        if s[j] == '>':
            l_large_rank[j] = len(large_idx)

            large_idx.append(j)

    for j in range(n-1, -1, -1):
        if j == n - 1:
            r_less_sum[j] = 0
        else:
            r_less_sum[j] = r_less_sum[j + 1] + len(less_idx)

        if len(less_idx) > 0:
            r_nearest_less[j] = less_idx[-1]
        else:
            r_nearest_less[j] = n

        r_less_count[j] = len(less_idx)

        if s[j] == '<':
            r_less_rank[j] = len(less_idx)

            less_idx.append(j)

    output = [0] * n
    # print(large_idx, less_idx)
    # print(l_nearest_large, r_nearest_less)
    # print(l_large_rank, r_less_rank)
    # print(l_large_sum, r_less_sum)

    for j in range(n):
        if s[j] == '<':
            if l_large_count[j] <= r_less_count[j]:
                # go to left
                if l_large_count[j] == 0:
                    output[j] = j + 1
                else:
                    l_output = l_large_sum[j]

                    r_nearest_less_pos = r_nearest_less[j]
                    r_nearest_less_rank = r_less_rank[r_nearest_less_pos]
                    r_turn_less_rank = r_nearest_less_rank - (l_large_count[j] - 1)
                    r_turn_less_idx = less_idx[r_turn_less_rank]
                    r_output = r_less_sum[j] - r_less_sum[r_turn_less_idx] - (r_turn_less_idx - j) * r_turn_less_rank

                    output[j] = (l_output + r_output) * 2 + j + 1
            else:
                # go to right
                if r_less_count[j] == 0:
                    l_nearest_large_idx = l_nearest_large[j]
                    l_nearest_large_rank = l_large_rank[l_nearest_large_idx]
                    l_output = l_large_sum[j] - l_large_sum[l_nearest_large_idx] - (
                                j - l_nearest_large_idx) * l_nearest_large_rank

                    output[j] = l_output * 2 + n - j
                else:
                    r_output = r_less_sum[j]

                    l_nearest_large_pos = l_nearest_large[j]
                    l_nearest_large_rank = l_large_rank[l_nearest_large_pos]
                    l_turn_large_rank = l_nearest_large_rank - (r_less_count[j] - 1)
                    l_turn_large_idx = large_idx[l_turn_large_rank]
                    l_output = l_large_sum[j] - l_large_sum[l_turn_large_idx] - (
                            j - l_turn_large_idx) * l_turn_large_rank

                    output[j] = (l_output + r_output) * 2 + (n - j)

        elif s[j] == '>':
            if l_large_count[j] >= r_less_count[j]:
                # go right
                if r_less_count[j] == 0:
                    output[j] = n - j
                else:
                    r_output = r_less_sum[j]

                    l_nearest_large_pos = l_nearest_large[j]
                    l_nearest_large_rank = l_large_rank[l_nearest_large_pos]
                    l_turn_large_rank = l_nearest_large_rank - (r_less_count[j] - 1)
                    l_turn_large_idx = large_idx[l_turn_large_rank]
                    l_output = l_large_sum[j] - l_large_sum[l_turn_large_idx] - (
                            j - l_turn_large_idx) * l_turn_large_rank

                    output[j] = (l_output + r_output) * 2 + (n - j)
            else:
                # go to left
                if l_large_count[j] == 0:
                    r_nearest_less_idx = r_nearest_less[j]
                    r_nearest_less_rank = r_less_rank[r_nearest_less_idx]
                    r_output = r_less_sum[j] - r_less_sum[r_nearest_less_idx] - (
                            r_nearest_less_idx - j) * r_nearest_less_rank

                    output[j] = r_output * 2 + j + 1
                else:
                    l_output = l_large_sum[j]

                    r_nearest_less_pos = r_nearest_less[j]
                    r_nearest_less_rank = r_less_rank[r_nearest_less_pos]
                    r_turn_less_rank = r_nearest_less_rank - (l_large_count[j] - 1)
                    r_turn_less_idx = less_idx[r_turn_less_rank]
                    r_output = r_less_sum[j] - r_less_sum[r_turn_less_idx] - (r_turn_less_idx - j) * r_turn_less_rank

                    output[j] = (l_output + r_output) * 2 + j + 1

    for o in output:
        print(o, end=' ')
    print('')

