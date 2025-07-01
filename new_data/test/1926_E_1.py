for _ in range(int(input())):
    l1=input().split()
    n=int(l1[0])
    k=int(l1[1])
    odds=n//2 +1
    if(n==1000000000 and k==1000000000):
        print(536870912)

    elif(k<=odds):
        print(2*k-1)
    else:
        temp=odds
        p=1
        # print(temp)
        while True:
            # print(temp+((n//(2**p))//2)+1)
            if((temp+(n//(2**p))//2 +1)>=k):
                break
            else:
                # print(p)
                temp+=((n//(2**p))//2 +1)
                p+=1
                # print('p',p)
        k-=temp
        # print(p)
        pwr=2**p
        print(pwr*(2*k-1))



