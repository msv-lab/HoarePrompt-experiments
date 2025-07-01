t = int(input())
ans = 2
for i in range(t):
  n = int(input())
  if n < 2:
    ans = 1
  else:
    while ans * 2 <= n:
      ans *= 2
  print(ans)