n = int(input())
cubes = [list(map(int, input().split())) for _ in range(n)]

digits = set()
for cube in cubes:
    digits.update(str(digit) for digit in cube)

if '0' in digits:
    digits.remove('0')

max_num = int(''.join(sorted(digits, reverse=True)))
print(max_num)
