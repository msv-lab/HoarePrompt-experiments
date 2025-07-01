from sys import stdin

res = []
i = 0
l = ""

for ligne in stdin:

    if i == 0:
        nb_test = int(ligne)

    elif i % 2 == 1:
        l = ligne.split()

    else:
        vaches = ligne.split()
        for j in range(len(vaches)):
            vaches[j] = int(vaches[j])

        k = int(l[1])
        val_vache = vaches[k - 1]
        inversion = False
        i_sup_vache = None

        for j in range(len(vaches)):
            if vaches[j] > val_vache:
                i_sup_vache = j
                if i_sup_vache < (k - 1):
                    inversion = True
                break

        if inversion:
            vaches[k - 1], vaches[i_sup_vache] = vaches[i_sup_vache], vaches[k - 1]
            k = i_sup_vache + 1

        res = 0

        if k > 1:
            if vaches[k - 1] > vaches[k - 2]:
                res += 1

        for j in range(k - 1, len(vaches) - 1):
            if vaches[j] > vaches[j + 1]:
                res += 1
            else:
                break

        print(res)

    i += 1