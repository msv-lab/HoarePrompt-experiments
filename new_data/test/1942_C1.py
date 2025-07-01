def solve():
	nhap = list(map(int,input().split()))
	a = list(map(int,input().split()))
	n = nhap[0]
	x = nhap[1]
	y = nhap[2]

	if n > 2 * (10**5):
		x = 2 * (10**5)


	kq = x - 2;
	a.sort()

	for i in range (len(a) - 1):
		if a[i+1] - a[i] == 2:
			kq +=1

	if  n - a[len(a)-1] + a[0] - 1 ==1:
		kq += 1

	print(kq)

t = int(input())
while t > 0:
	t -= 1
	solve()