def sort_list():
    global m_dg
    abs_list = []
    sorted_list = []
    max_dis = 0
    lh = len(h_list)
    for i in x_list:
        absnum = abs(i)
        abs_list.append(absnum)
        if absnum > max_dis:
            max_dis = absnum
    m_dg = sum(h_list) / max_dis
    if k < m_dg:
        ans_list.append("NO")
        return False
    elif k > 2 * m_dg:
        ans_list.append("YES")
        return True
    for i in range(lh):
        cindex = abs_list.index(min(abs_list))
        sorted_list.append([h_list[cindex], x_list[cindex]]) # h, x
        h_list.pop(cindex)
        x_list.pop(cindex)
        abs_list.pop(cindex)
    return sorted_list


def process(s_list):
    while True:
        n = k
        indx = 0
        saveh = 0
        while (n > 0) and (s_list[indx][0] > 0):
            saveh = s_list[indx][0]
            s_list[indx][0] = s_list[indx][0] - n
            n = n - saveh
            if len(s_list)-1 > indx:
                indx += 1
        for i in range(indx+1):
            if s_list[0][0] <= 0:
                s_list.pop(0)
        if len(s_list) == 0:
            ans_list.append("YES")
            return None
        for i in range(len(s_list)):
            if s_list[i][1] > 0:
                s_list[i][1] = s_list[i][1] - 1
            if s_list[i][1] < 0:
                s_list[i][1] = s_list[i][1] + 1
            if s_list[i][1] == 0:
                ans_list.append("NO")
                return None


def start():
    global x_list, h_list, k, ans_list, max_h
    ans_list = []
    t_run = int(input())
    for i in range(t_run):
        n, k = input().split()
        n, k = int(n), int(k)
        h_list = input().split()
        h_list = list(map(lambda x: int(x), h_list))
        x_list = input().split()
        x_list = list(map(lambda x: int(x), x_list))
        max_h = max(h_list)
        if k >= 2 * max_h:
            ans_list.append("YES")
            continue
        sl = sort_list()
        if sl == False:
            continue
        if sl == True:
            continue
        process(sl)
    for i in ans_list:
        print(i)


start()