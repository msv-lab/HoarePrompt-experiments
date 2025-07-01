cases = int(input())

for c in range(cases):
    na_frente, pos_final = map(int, input().split())
    custo_pra_trocar_a = list(map(int, input().split()))
    custo_pra_passar_b = list(map(int, input().split()))

    na_frente -= 1
    pos_final -= 1

    total = 0
    best = 10 ** 12
    for v in range(na_frente, -1, -1):
        if (v <= pos_final):
            if (best > total + custo_pra_trocar_a[v]):
                best = total + custo_pra_trocar_a[v]

            if (custo_pra_trocar_a[v] < custo_pra_passar_b[v]):
                total += custo_pra_trocar_a[v]
            else:
                total += custo_pra_passar_b[v]
        else:
            if (custo_pra_trocar_a[v] < custo_pra_passar_b[v]):
                total += custo_pra_trocar_a[v]
            else:
                total += custo_pra_passar_b[v]

    print(best)








