
t = int(input())
res=[]
for i in range(t):
  b = str(input())
  n, k, x = b.split(" ")
  n, k, x = int(n), int(k), int(x)

  a = list(map(int, str(input()).split(" ")))
  a.sort(reverse=True)
  pre = [0] * (n+1)

  for i in range(1, n+1, 1):
    pre[i] = pre[i-1] + a[i-1]

  curr_sum = sum(a)
  ans = -100000000
  for i in range(k+1):
    # Slide the window
    bob = pre[min(i+x, n)] - pre[i] # the min is here to enforce limit on rhs
    ans = max(ans, curr_sum - 2*bob)
    if i < k:
      curr_sum -= a[i]
  res.append(ans)

for r in res:
  print(r)




