def ye(n,li):
    year = [0]*n
    for idx,value in enumerate(li):
        for j in range(1,1000):
            if year[idx-1] < value *j:
                year[idx]= value *j
                break

    return year[-1]
t = int(input())

for _ in range(t):
    n = int(input())
    a_list = list(map(int,input().split()))
    print(ye(n,a_list))
