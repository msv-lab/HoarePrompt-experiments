def find_max_x(n, cubes):
    from itertools import product

    # Create a set for each cube's faces
    cube_faces = [set(cube) for cube in cubes]

    def can_form_number(num):
        digits = list(str(num))
        used_cubes = [False] * n

        for digit in digits:
            found = False
            for i in range(n):
                if not used_cubes[i] and digit in cube_faces[i]:
                    used_cubes[i] = True
                    found = True
                    break
            if not found:
                return False
        return True

    x = 0
    while can_form_number(x + 1):
        x += 1

    return x

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    cubes = []
    index = 1
    
    for i in range(n):
        cubes.append(data[index:index + 6])
        index += 6

    print(find_max_x(n, cubes))
