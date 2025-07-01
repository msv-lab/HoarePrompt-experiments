R = lambda: map(int, input().split())
t,=R()
while t:
    t -= 1
    n,x,y= R()
    sx=0;
    l = list(R())
    l.append(n+l[0])
    l.sort()
    mi=9999
    for i in range(1,x+1):
        if l[i]-l[i-1]==2 :
            sx+=1
    cons=x+sx-2
    cons=min(n-2,cons)
    print(cons)  # 使用 print 函数打印列表元素，而不是调用 P 函数
