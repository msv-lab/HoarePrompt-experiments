def make_space(a,b,c):
    result=a
    if b%3!=0:
        remaining=b-((b//3)*3)
        if remaining>c:
            result=-1
        else:
            if remaining+c<3:
                result=-1
            else:
                result+=(b//3) + 1
                c-=(3-remaining)
                if c%3==0:
                    result+=c//3
                else:
                    result+=(c//3)+1
    else:
        result+=b//3
        if c%3==0:
            result+=c//3
        else:
            result+=(c//3)+1
    return result


amount=int(input())
while amount>0:
    a,b,c = map(int, input().split())
    result=make_space(a,b,c)
    print(result)
    amount-=1