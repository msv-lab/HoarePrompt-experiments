n = int(input())
for _ in range(n):
    a,b,c = map(int,input().split())
    if a < b:
        if b < c:
            print("STAIR")
        else:
            print("PEAK")
    else:
        print("NONE")