n = int(input())
b=[]
for i in range(n):
    x = int(input())
    b.append(x)
'''b = list(map(int, input().split("\n")))'''
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(n):
    if(b[i]<=26):
        print(a[0],a[0],a[b[i]-3],sep="")
    elif(b[i]<=52):
        print(a[0],a[b[i]-28],a[25],sep="")
    elif(b[i]<=78):
        print(a[b[i]-53],a[25],a[25],sep="")
    else:
        print(" ")