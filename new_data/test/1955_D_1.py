for i in range(int(input())):
  n,m,k=map(int,input().split())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  U=[False for j in range(n)]
  S=dict()
  for j in range(m):
    if B[j] in S:
      S[B[j]]+=1
    else:
      S[B[j]]=1
  size=m
  D=dict()
  for j in range(m):
    if A[j] in S:
      if S[A[j]]:
        S[A[j]]-=1
        size-=1
        U[j]=True
      else:
        if A[j] in D:
          D[A[j]].append(j)
        else:
          D[A[j]]=[j]
    else:
      if A[j] in D:
        D[A[j]].append(j)
      else:
        D[A[j]]=[j]
  ans=int(size<=m-k)
  for j in range(1,n-m+1):
    if U[j-1]:
      U[j-1]=False
      S[A[j-1]]+=1
      size+=1
      if A[j-1] in D:
        if D[A[j-1]]:
          U[D[A[j-1]].pop()]=True
          size-=1
          S[A[j-1]]-=1
    if A[j+m-1] in S:
      if S[A[j+m-1]]:
        S[A[j+m-1]]-=1
        size-=1
        U[j+m-1]=True
      else:
        if A[j+m-1] in D:
          D[A[j+m-1]].append(j+m-1)
        else:
          D[A[j+m-1]]=[j+m-1]
    if size<=m-k:
      ans+=1
  print(ans)