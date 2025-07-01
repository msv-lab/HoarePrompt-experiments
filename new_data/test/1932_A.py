t = int(input())
while not(1<=t<=1000):
    t = int(input())
resualt =""
for i in range(t):
    coins=0
    n = int(input())
    while not(1<=n<=50):
        n = int(input())
    path = input()
    while not(len(path)==n):
        path = input()
    p = path.find("**")
    if p!=-1:
        path=path[0:p]
    for i in range(len(path)):
        if path[i]=="@":
            coins+=1
    resualt += str(coins)
for i in range(len(resualt)):
    print(resualt[i])
