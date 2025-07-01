t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    m = s.count("map")
    s = s.replace("map", "")

    p = s.count("pie")
    print(m + p)

