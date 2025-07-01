n=int(input())
for i in range(n):
  k=int(input())
  l=list(map(int,input().split()))
  for h in range(1,k):
    t=l[h]
    for j in range(1,10000):
      if(j*t>l[h-1]):
        l[h]=j*t
        break
  print(l[k-1])