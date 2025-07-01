def can_send_all_messages(t, data):
    results = []
    for i in range(t):
        n, f, a, b = data[i][0], data[i][1], data[i][2], data[i][3]
        moments = data[i][4]

        min_energy = f
        for i in range(n):
            energy_required = moments[i] * a
            if moments[i] * a > b:
                energy_required -= (moments[i] - 1) * b

            min_energy = min(min_energy, f - energy_required)

        results.append("YES" if min_energy > 0 else "NO")

    return results

t = int(input())
data = []
for _ in range(t):
    n, f, a, b = map(int, input().split())
    moments = list(map(int, input().split()))
    data.append((n, f, a, b, moments))

results = can_send_all_messages(t, data)
for result in results:
    print(result)
