import sys
import math


class Fenw:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        # i: índice 0-based
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        # Suma de [0, i] (i 0-based)
        s = 0
        i += 1
        while i:
            s += self.tree[i]
            i -= i & -i
        return s

    def query_range(self, l, r):
        return self.query(r) - (self.query(l - 1) if l > 0 else 0)

    def find_kth(self, k):
        """Encuentra el índice mínimo i tal que query(i) >= k"""
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)
        while bit_mask:
            t = idx + bit_mask
            if t <= self.n and self.tree[t] < k:
                k -= self.tree[t]
                idx = t
            bit_mask //= 2
        return idx  # idx es 0-based


def solve():
    data = sys.stdin.read().split()
    ptr = 0
    t = int(data[ptr])
    ptr += 1
    out_lines = []

    for _ in range(t):
        n = int(data[ptr])
        ptr += 1
        v = list(map(int, data[ptr:ptr + n]))
        ptr += n
        p = list(map(int, data[ptr:ptr + n]))
        ptr += n
        # Ajustar a 0-indexed
        p = [x - 1 for x in p]

        # Precalcular el "umbral" para cada seta.
        # zero_at_k[i] es el mayor k para el cual la seta i está activa (disponible)
        # Se inicializa con n+2 y se actualiza para k>=2 usando p.
        zero_at_k = [n + 2] * n
        for k in range(2, n + 1):
            # Para la seta con índice p[k-2], se anula a partir de k,
            # es decir, está activa solo hasta k-1.
            zero_at_k[p[k - 2]] = k - 1

        # Armar una lista de setas: (magia, umbral)
        mushrooms = [(v[i], zero_at_k[i]) for i in range(n)]
        # Ordenar por magia decreciente; en caso de empate, por índice (no relevante aquí)
        sorted_mushrooms = sorted(mushrooms, key=lambda x: -x[0])

        # Preparar BIT: cada posición representa una seta en sorted_mushrooms.
        BIT = Fenw(n)
        for i in range(n):
            BIT.update(i, 1)

        # Para actualizar el BIT según el umbral,
        # preparamos una lista de (umbral, pos) donde pos es la posición de la seta
        # en sorted_mushrooms.
        removal = []
        for pos, (magic, thresh) in enumerate(sorted_mushrooms):
            removal.append((thresh, pos))
        removal.sort(key=lambda x: x[0])  # en orden ascendente por umbral

        max_strength = 0
        best_k = 0
        limit = min(n, 2000)
        rem_ptr = 0
        # Para k = 1 a limit, actualizamos BIT removiendo las setas que dejan de estar disponibles.
        for k in range(1, limit + 1):
            # Remover todas las setas cuyo umbral < k
            while rem_ptr < n and removal[rem_ptr][0] < k:
                pos_to_remove = removal[rem_ptr][1]
                BIT.update(pos_to_remove, -1)
                rem_ptr += 1

            available = BIT.query(n - 1)
            if available < k:
                continue
            # Encontrar el k-ésimo disponible (0-based: find_kth(k) devuelve índice)
            pos_k = BIT.find_kth(k)
            # En sorted_mushrooms, pos_k corresponde a la seta con la k-ésima mayor magia entre las disponibles
            kth_magic = sorted_mushrooms[pos_k][0]
            strength = k * kth_magic
            if strength > max_strength or (strength == max_strength and k < best_k):
                max_strength = strength
                best_k = k

        # Verificación adicional para k=1: la seta más poderosa sola
        if sorted_mushrooms[0][0] > max_strength:
            max_strength = sorted_mushrooms[0][0]
            best_k = 1

        out_lines.append(f"{max_strength} {best_k}")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()
