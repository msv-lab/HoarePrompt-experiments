a = int(input())
b = int(input())
c = int(input())

min_lemon = min(a, b//2, c//4)
print(min_lemon + min_lemon*2 + min_lemon*4)
