t = int(input())


# k=[]
def help(l, turn):
    h = l[0]
    w = l[1]
    xa = l[2]
    ya = l[3]
    xb = l[4]
    yb = l[5]
    # print(xa,ya,xb,yb,)
    # base case
    if turn:
        k = "Alice"
        k1 = "Bob"
    else:
        k1 = "Alice"
        k = "Bob"
    if xa >= xb:
        return "Draw"
    elif abs(xa - xb) == 1:
        if abs(ya - yb) <= 1:
            return k
        else:
            return "Draw"
    # elif abs(xa-xb)==2:
    #     if abs(ya-yb)<=1:
    #         return k1
    #     else:
    #         return "Draw"
    else:
        if turn:
            diff = (xb - xa) % 2
            if diff:
                chk = yb - ya
                if chk == 0:
                    l[2] += 1
                    return help(l, not turn)
                elif chk > 0:
                    l[2] += 1
                    l[3] += 1
                    return help(l, not turn)
                else:
                    l[2] += 1
                    l[3] -= 1
                    return help(l, not turn)
            else:
                chk = ya - yb
                if chk == 0:
                    if h - ya > ya - 1:
                        if ya + 1 <= h:
                            # go right
                            l[2] += 1
                            l[3] += 1
                            return help(l, not turn)
                        else:
                            # go down
                            l[2] += 1
                            return help(l, not turn)
                    else:
                        if ya - 1 >= 1:
                            # go left
                            l[2] += 1
                            l[3] -= 1
                            return help(l, not turn)
                        else:
                            # go down
                            l[2] += 1
                            return help(l, not turn)
                elif chk > 0:
                    if ya + 1 <= h:
                        # go right
                        l[2] += 1
                        l[3] += 1
                        return help(l, not turn)
                    else:
                        # go down
                        l[2] += 1
                        return help(l, not turn)
                else:
                    if ya - 1 >= 1:
                        # go left
                        l[2] += 1
                        l[3] -= 1
                        return help(l, not turn)
                    else:
                        # go down
                        l[2] += 1
                        return help(l, not turn)
        else:
            diff = (xb - xa) % 2
            if diff:
                # attack
                chk = ya - yb
                if chk == 0:
                    l[4] -= 1
                    return help(l, not turn)
                elif chk > 0:
                    l[4] -= 1
                    l[5] += 1
                    return help(l, not turn)
                else:
                    l[4] -= 1
                    l[5] -= 1
                    return help(l, not turn)
            else:
                # escape
                chk = yb - ya
                if chk == 0:
                    if h - yb > yb - 1:
                        if yb + 1 <= h:
                            # go right
                            l[4] -= 1
                            l[5] += 1
                            return help(l, not turn)
                        else:
                            # go up
                            l[4] -= 1
                            return help(l, not turn)
                    else:
                        if yb - 1 >= 1:
                            # go left
                            l[4] -= 1
                            l[5] -= 1
                            return help(l, not turn)
                        else:
                            # go up
                            l[4] -= 1
                            return help(l, not turn)
                elif chk > 0:
                    if yb + 1 <= h:
                        # go right
                        l[4] -= 1
                        l[5] += 1
                        return help(l, not turn)
                    else:
                        # go down
                        l[4] -= 1
                        return help(l, not turn)
                else:
                    if yb - 1 >= 1:
                        # go left
                        l[4] -= 1
                        l[5] -= 1
                        return help(l, not turn)
                    else:
                        # go down
                        l[4] -= 1
                        return help(l, not turn)
        # help(l,not turn)


for i in range(t):
    l = list(map(int, input().split()))

    print(help(l, True))