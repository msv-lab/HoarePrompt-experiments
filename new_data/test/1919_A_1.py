t = int(input())
results = []

for _ in range(t):
    a, b = map(int, input().split())
    if a == 1 and b == 1:
        results.append("Bob")
    elif a == 1 or b == 1:
        results.append("Alice")
    else:
        results.append("Bob" if (a + b) % 2 == 0 else "Alice")

for result in results:
    print(result)
