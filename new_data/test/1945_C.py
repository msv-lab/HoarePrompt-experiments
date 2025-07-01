import math
from decimal import Decimal

t = int(input())
while t:
    n=int(input())
    input_string = input()
    arr = [int(ch) for ch in input_string]
    z = arr.count(0)
    o = arr.count(1)
    z_r = z
    o_r = o
    z_l=0
    o_l=0
    dist,ans,pos=abs(n/2),0,0
    if o_r>=(z_r+o_r)/2:
        b_d=dist
    else:
        b_d=30001
    for i in arr:
        pos+=1
        if i==0:
            z_l+=1
            z_r-=1
        else:
            o_l+=1
            o_r-=1
        if o_r>=((z_r+o_r)/2) and z_l>=((z_l+o_l)/2) and b_d > abs(n/2-pos):
            ans=pos
            b_d = abs(n/2-pos)
    print(ans)
    t -= 1