def solve():
	n = int(input())
	s = input()
	neg = 0
	for i in s:
		if i=='-':neg+=1
	print(n-2*neg if n!=neg else n)
t = int(input())
while t:
	solve()
	t-=1