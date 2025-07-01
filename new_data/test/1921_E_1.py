for _ in range(int(input())):
    h, w, xa, ya, xb, yb = map(int, input().split())
    if xb <= xa or (abs(yb - ya) >= abs(xb - xa)):
        print("DRAW")
    else:
        if (xb - xa) % 2 == 1:  # ALICE ka mauka
            if yb == ya or abs(yb - ya) == 1:
                print("ALICE")
            elif yb > ya:
                if abs(yb - ya) >= (abs(xb - xa)) - 2 * (w - yb) or (w - yb) >= abs(xa - xb):
                    print("DRAW")
                else:
                    print("ALICE")
            else:
                if abs(yb - ya) >= (abs(xb - xa)) - 2 * (yb - 1) or yb >= abs(xb - xa):
                    print("DRAW")
                else:
                    print("ALICE")
        else:  # BOB ka mauka
            if yb == ya:
                print("BOB")
            elif yb > ya:
                if abs(yb - ya) >= (abs(xb - xa)) - 2 * (ya - 1) or ya >= abs(xb - xa):
                    print("DRAW")
                else:
                    print("BOB")
            else:
                if abs(yb - ya) >= (abs(xb - xa)) - 2 * (w - ya) or (w - ya) >= abs(xb - xa):
                    print("DRAW")
                else:
                    print("BOB")




