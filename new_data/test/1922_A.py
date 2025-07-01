t = int(input())
for _ in range(t):
	n = int(input())
	a = input()
	b = input()
	c = input()

	template_found = True
	for i in range(n):
		if c[i] == a[i] and c[i] == b[i]:
			continue
		elif c[i] != a[i] and c[i] != b[i]:
			continue
		elif c[i] == a[i] and c[i] != b[i]:
			if a[i].islower():
				template_found = False
				break
		elif c[i] != a[i] and c[i] == b[i]:
			if b[i].islower():
				template_found = False
				break

	print("YES" if template_found else "NO")