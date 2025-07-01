T=int(input())
for i in range(T):
    a,b = map(int, input().split())
    if a==b:
        print("Bob")
    else:
        if a==1:
            print("Alice")
        elif b==1:
            print("Bob")
        else:
            if a%2==1:
                print("Bob")
            elif a%2==0 and b%2==1:
                print("Alice")
            else:
                if a>b:
                    print("Bob")
                else:
                    print("Alice")