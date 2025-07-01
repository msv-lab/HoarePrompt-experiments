q=0
k=0
a=int(input())
for i in range(a):
    b=int(input())
    c=input()
    if c.count('+')==0:
        print(c.count('-'))
    elif c.count('-')==0:
        print(c.count('+'))
    else:
        print(c.count('+')-c.count('-'))