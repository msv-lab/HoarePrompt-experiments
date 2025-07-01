t = int(input())
ans = 2
for i in range(t):
    n = int(input())
    if n < 2:
        ans = 1
    else:
        while ans * 2 <= n:
            ans *= 2
    print(ans)

# t = int(input())
# for i in range(t):
#   n, m, k = map(int, input().split())
#   b = list(map(int, input().split()))
#   c = list(map(int, input().split()))
#   lst = []
#   for f in range(n):
#     for s in range(m):
#       if b[f] + c[s] <= k:
#         lst.append([f, s])
#   print(len(lst))

# from math import gcd
# a, b, c, d = map(int, input().split() )
# Sx = abs(c - a)
# Sy = abs(d - b)
# print(Sx + Sy - gcd(Sx, Sy))

# from math import gcd
# a, b = map(int, input().split())
# print(a // gcd(a, b), b // gcd(a, b))

# from math import gcd
# a, b = map(int, input().split())
# print((a*b) // gcd(a, b))

# t = int(input())
# for i in range(t):
#   n = int(input())
#   a = list(map(int, input().split()))
#   s = 0
#   for i in range(n):
#     s += abs(a[i])
#   print(s)


# 27
# Дана последовательность целых чисел. Необходимо найти максимально возможную сумму её непрерывной подпоследовательности, в которой количество положительных нечётных элементов кратно k  =  30.

# A = open('27-B (11).txt')
# k = 30
# n = int(A.readline())
# data = [int(x) for x in A]
# maxSum = 0
# prefix = [0]
# count = 0
# d = [0] * k
# for i in range(n):
#   prefix.append(prefix[-1] + data[i])
#   if data[i] > 0 and data[i] % 2 != 0:
#     count += 1
#   maxSum = max(maxSum, prefix[i+1] - d[count % k])
#   d[count % k] = min(d[count % k], prefix[i+1])
# print(maxSum)


# A = open('27-B.txt')
# k = 30
# n = int(A.readline())
# a = [int(x) for x in A]
# maxSumA = 0
# t = 0
# while t <= n-1:
#   countA = 0
#   sumA = 0
#   for i in range(t, len(a)):
#     sumA += a[i]
#     if a[i] > 0 and a[i] % 2 != 0:
#       countA += 1
#     if countA % k == 0:
#       maxSumA = max(maxSumA, sumA)
#   t += 1

# print(maxSumA)


# f = open('26 (1).txt')
# n, m = map(int, f.readline().split())
# a = [int(i) for i in f]
# count = 0
# s = 0
# b = []
# for i in range(len(a)):
#   if 210 <= a[i] <= 220:
#     count += 1
#     s += a[i]
#   else:
#     b.append(a[i])
# b = sorted(b)
# i = 0
# while i < len(b) and s + b[i] <= m:
#   s += b[i]
#   i += 1
#   count += 1
# print(count)
# i -= 1
# print(b[i-2], b[i])
# while i + 1 < len(b) and s - b[i] + b[i + 1] <= m:
#   s = s - b[i] + b[i + 1]
#   i += 1
# print(b[i], s)


# for i in range(int(289_123_456 ** 0.25), int(389_123_456 ** 0.25)):
#   for j in range(2, i):
#       if not i % j:  # Проверка на простое число
#           break
#   else:
#       print(i ** 4, i ** 3)


# 25
# count = 0
# ans = []
# maxDiv = 0
# start = int(289123456**0.5) + 1
# finish = int(389123456**0.5) + 1
# for i in range(start, finish):
#   divs = []
#   for j in range(2, i + 1):
#     if (i**2) % j == 0:
#       divs.append(j)
#       # print('OK')
#       if j != (i**2) // j:
#         divs.append((i**2) // j)
#   if len(divs) == 3:
#     # print('OK')
#     ans.append([i**2, max(divs)])
# print(sorted(ans))


# 24
# f = open('24 (1).txt')
# a = f.readline()
# count = 0
# max_count = 0
# i = 0
# while i < len(a)-2:
#   if a[i] in 'CDF' and a[i+1] in 'CDF' and a[i+2] in 'AO':
#     count += 1
#     max_count = max(max_count, count)
#     i += 3
#   else:
#     i += 1
#     count = 0
# print(max_count)


# CCADDO

# f = open('17 (1).txt')
# a = [int(x) for x in f]
# pairs = 0
# minN3 = 100000
# maxSum = 0
# for i in range(len(a)):
#   if 99 < a[i] < 1000 and a[i] % 10 == 3:
#     minN3 = min(minN3, a[i])
# for i in range(len(a)-1):
#   if (999 < a[i] < 10000 and (a[i+1] < 1000 or a[i+1] > 9999)) or (999 < a[i+1] < 10000 and (a[i] < 1000 or a[i] > 9999)):
#     if (a[i]**2 + a[i+1]**2) % minN3 == 0:
#       pairs += 1
#       maxSum = max(maxSum, a[i]**2 + a[i+1]**2)

# print(pairs, maxSum)

# def F(n):
#   if n <= 3:
#     if n == 1:
#       return 0
#     elif n == 2:
#       return 1
#     elif n == 3:
#       return 1
#   else:
#     return F(n-3) + F(n-2) + F(n-1)
# print(F(11))


# lett = 'ВЛТУ'
# a = ['' for i in range(76)]
# a[0] = ''
# a[1] = 'ВВВВ'
# for i in range(2, 76):
#   for j in lett:
#     a.append(a[i][1:] + j)
# print(a[75])

# from turtle import *
# scale = 20
# c = 3
# while c > 0:
#   c -= 1
#   forward(7 * scale)
#   right(90)
# forward(8 * scale)
# c = 3
# while c > 0:
#   c -= 1
#   left(90)
#   forward(5 * scale)
# penup()
# for x in range(-200,200, scale):
#   for y in range(-200,200, scale):
#     setposition(x,y)
#     dot(5, 'red')
# done()

# ((y → x) ≡ (x → w)) ∧ (z ∨ x)
# print('x y z w F')
# for x in range(2):
#   for y in range(2):
#     for z in range(2):
#       for w in range(2):
#         F = ((y <= x) == (x <= w)) and (z or x)
#         print(x, y, z, w, int(F))

# n = int(input())
# arr = []
# ans = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))
# for i in range(n // 2 + 1):
#   ans.append(arr[i][n // 2 + i])
# for i in range(n // 2 + 1, n):
#   ans.append(arr[i][])

# print(*ans)

# import string
# a, b = input().split()
# d1 = dict().fromkeys(string.ascii_lowercase, 0)
# d2 = dict().fromkeys(string.ascii_lowercase, 0)
# for i in a:
#   d1[i] += 1
# for i in b:
#   d2[i] += 1
# ans = 0
# for letter in string.ascii_lowercase:
#   ans += max(0, d2[letter] - d1[letter])
# print(ans)

# n, c1, c2 = map(int, input().split())
# maxN = 0
# ans = 0
# for i in range(c1, c2 + 1):
#   t = n
#   ost = ''
#   while t > 0:
#     ost += str(t % i)
#     if t % i >= maxN:
#       maxN = t % i
#       ans = i
#     # maxN  = max(maxN, t % i)
#     t = t // i
# print(ans)


# from math import gcd
# a, b = map(int, input().split())
# if gcd(a,b) == 1:
#     print("YES")
# else:
#   for i in range(2, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#       print(i)
#       break

# def f(n):
#   binN = str(bin(n))
#   even = int(binN.count('0'))
#   odd = int(binN.count('1'))
#   if even > odd:
#     binN += '1'
#   elif even < odd:
#     binN += '0'
#   elif even == odd:
#     if n % 2 == 0:
#       binN += '0'
#     else:
#       binN += '1'
#   return binN

# for n in range(876544, 1234567900):
#   r = int(f(f(f(n))))


# F1  =  (x∨¬y)≡(z→w)
# F2  =  (¬x≡y)∧(z→w)

# print('x y z w F1 F2')
# for x in range(0, 2):
#   for y in range(0, 2):
#     for z in range(0, 2):
#       for w in range(0, 2):
#         F1 = (x or (not y)) == (z <= w)
#         F2 = (not x == y) and (z <= w)
#         print(x, y, z, w, int(F1), int(F2))


# t = int(input())
# for i in range(t):
#   mx = 0
#   c = 0
#   n, k = map(int, input().split())
#   s = input()
#   r, l = 0, 0
#   while r < n - 1:
#     while r < n-1 and c <= k:
#       mx = max(mx, r - l + 1)
#       if s[r] != s[r+1]:
#         c += 1
#       r += 1
#     if c > k:
#       while l < n-1 and s[l] == s[l+1]:
#         l += 1
#       if s[l] != s[l+1]:
#         c -= 1
#         l += 1
#   print(mx)


# t = int(input())
# for i in range(t):
#   ans = ''
#   n, m = map(int, input().split())
#   a = list(map(int, input().split()))
#   b = list(map(int, input().split()))
#   min1 = n
#   min2 = m
#   max1 = sum(a)
#   max2 = sum(b)
#   if max1 > min2:
#     ans += 'Y'
#   else:
#     ans += 'N'
#   if min(max1,max2) >= max(min1,min2):
#     ans += 'Y'
#   else:
#     ans += 'N'
#   if max2 > min1:
#     ans += 'Y'
#   else:
#     ans += 'N'
#   print(ans)


# f = open('17.txt')
# a = [int(x) for x in f]
# lst = []
# k = 0
# minEl = 10001
# for i in a:
#   if i % 10 == (i // 10) % 10:
#     minEl = min(i, minEl)
# for i in range(len(a)-1):
#   if abs(a[i] % 10) == abs((a[i+1] // 10) % 10) or abs(a[i+1] % 10) == abs((a[i] // 10) % 10):
#     if (a[i] % 7 == 0 and a[i+1] % 7 != 0) or (a[i+1] % 7 == 0 and a[i] % 7 != 0):
#       if a[i]**2 + a[i+1]**2 <= minEl**2:
#         k += 1
#         lst.append(a[i]**2 + a[i+1]**2)
# print(k, max(lst))


# def F(n):
#   if n < 9:
#     return n
#   return F(n % 9) + F(n // 9)
# k = 0
# for n in range(4*(6**20), 5*(6**20) + 1):
#   if F(n) == 121:
#     k += 1
# print(k)

# for a in range(1, 300):
#   flag = True
#   for x in range(1, 300):
#     if not((x % a == 0) or (x % 21 != 0 and x % 35 != 0)):
#       flag = False
#       break
#   if flag:
#     print(a)


# n = 4 ** 34 + 5 * 4**22 + 4**13 + 2 * 4**9 + 82
# s = ''
# while n > 0:
#   s += str(n % 16)
#   n //= 16
# s = s[::-1]
# print(s)

# s = '1' + '9' * 100

# while '19' in s or '299' in s or '3999' in s:
#   if '19' in s:
#     s = s.replace('19', '2', 1)
#   if '299' in s:
#     s = s.replace('299', '3', 1)
#   if '3999' in s:
#     s = s.replace('3999', '1', 1)
# print(s)


# print('x', 'y', 'z', 'w')
# for x in range(0, 2):
#   for y in range(0, 2):
#     for z in range(0, 2):
#       for w in range(0, 2):
#         if not((z and y) or ((not(x) or z) == (not(y) or w))):
#           print(x, y, z, w)


# with open('28133_B (1).txt') as f:
#   N = int(f.readline())
#   data = [int(x) for x in f]
#   ans = 0
#   first = 0
#   second = 0
#   for i in range(N):
#     for j in range(i+1, N):
#       if data[i] > data[j] and (data[i] + data[j]) % 120 == 0:
#         # ans = max(ans, data[i] + data[j])
#         if data[i] + data[j] > ans:
#           ans = data[i] + data[j]
#           first = data[i]
#           second = data[j]
#   print(first, second)


# 26
# f = open('26.txt')
# S,N = map(int, f.readline().split())
# arr = [int(i) for i in f]
# i = 0
# arr.sort()
# while i < len(arr) and S - arr[i] >= 0:
#   S -= arr[i]
#   i += 1
# print(i)
# while i < len(arr) and S + arr[i - 1] - arr[i] >= 0:
#   S = S + arr[i - 1] - arr[i]
#   i += 1
# print(arr[i-1])


# 25

# ans = []
# for num in range(45000000, 50000001):
#   d = []
#   for i in range(1, int(num**0.5) + 1):
#     if num % i == 0:
#       d.append(i)
#     if (num // i) % 2 != 0 and num // i != i:
#       d.append(num // i)
#   if len(d) == 5:
#     ans.append(num)
# print(*ans)


# num = 132103049840
# d = []
# for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#       if i % 2 == 1:
#         if i == 8:
#           print(i, i % 2, 'a')
#         d.append(i)
#       if (num // i) % 2 != 0 and num // i != i:
#         d.append(num // i)
# print(d)

# 24
# f = open('24.txt')
# s = f.readline()
# count = 0
# arr = []
# minn = 10**6
# for i in range(len(s)):
#   if s[i] == 'W':
#     arr.append(i)
# for j in range(len(arr) - 129):
#   count = arr[j+129] - arr[j] + 1
#   if count < minn:
#     minn = count
# print(minn)

# def check(n):
#   l = [0] * 10
#   while n > 0:
#     digit = n % 10
#     l[digit] += 1
#     n //= 10
#   c = 0
#   for elem in l:
#     if elem != 0:
#       c += 1
#   if c < 3:
#     return True
#   return False
# mn = 10**9
# ans = 0
# for i in range(1999, 2030):
#   if check(i):
#     if abs(i - 2012) < mn:
#       mn = abs(i - 2012)
#       ans = i
# print(ans)

# t = int(input())
# for i in range(t):
#   p = 1
#   n = int(input())
#   num = list(map(int, input().split()))
#   for j in num:
#     p *= j
#   if p > 0:
#     print(1)
#     print(1, 0)
#   else:
#     print(0)


# 17
# f = open("17.txt")
# a = [int(i) for i in f]
# count, maxsum = 0, 0
# for i in range(9999):
#   for j in range(i+1, 10000):
#     if (a[i] + a[j]) % 10 == 0:
#       count += 1
#       maxsum = max(maxsum, a[i] + a[j])
# print(count, maxsum)
# Ответ:4999742 19990

# 16
# def F(n):
#     if n <= 2:
#         return n + 1
#     if n > 2:
#         return 2*F(n - 1) + F(n - 2)
# print(F(4))

# for n in range(1000):
#   s = '5' + n * '2'
#   sumd = 0
#   while '72' in s or '522' in s or '2222' in s:
#     if '72' in s:
#       s = s.replace('72', '2', 1)
#     if '522' in s:
#       s = s.replace('522', '27', 1)
#     if '2222' in s:
#       s = s.replace('2222', '5', 1)
#   for digid in s:
#     sumd += int(digid)
#   if sumd == 63:
#     print(n)
#     break


# f = open('n9.txt')
# ans = 0
# for line in f:
#   a = list(map(int, line.split()))
#   b = set(a)
#   num = sum(a) - sum(b)
#   if len(b) == 5 and num < (sum(b) - num) / (len(b) - 1):
#     ans += 1
# print(ans)
# f.close()


# for x in range(2):
#   for y in range(2):
#     for z in range(2):
#       for w in range(2):
#         if not(not((not(z) or w) and (not(x) == y)) or (x and z)):
#           print(x, y, z, w)

# 6
# f = open("27-B.txt")
# n = int(f.readline())
# a = [int(i) for i in f]
# ans = 0
# for i in range(n):
#   for j in range(i+1, n):
#     if (a[i] + a[j]) % 4 == 0 and (a[i] * a[j]) % 59049 == 0:
#       ans += 1
# print(ans)

# k = 59049
# data = []
# for d in range(2, k+1):
#   if k % d == 0:
#     data.append(d)
# print(data)

# 5
# f = open('1_27_A.txt')
# k = int(f.readline())
# n = int(f.readline())
# arr = [int(i) for i in f]
# maxNum = 0
# ans = 0
# for i in range(n):
#   maxNum = max(maxNum, arr[i])
#   if i + k < len(arr):
#     ans = max(ans, arr[i+k] + maxNum)
# print(ans)

# f = open('27-B (1).txt')
# n = int(f.readline())
# arr = [int(x) for x in f]
# arr0 = []
# arr1 = []
# arr2 = []
# for i in arr:
#   if i % 3 == 0:
#     arr0.append(i)
#   if i % 3 == 1:
#     arr1.append(i)
#   if i % 3 == 2:
#     arr2.append(i)
# arr0.sort(reverse=True)
# arr1.sort(reverse=True)
# arr2.sort(reverse=True)
# print(max( sum([arr0[0], arr1[0], arr2[0]]), sum(arr0[0:3]), sum(arr1[0:3]),
#          sum(arr2[0:3])))

# f = open('27-B_2.txt')
# n = int(f.readline())
# arr = [int(x) for x in f]
# max1 = max(arr)
# arr.remove(max1)
# max2 = max(arr)
# while (max1 * max2) % 14 != 0:
#   arr.remove(max2)
#   max2 = max(arr)
# print(max1*max2)
# f.close()

# A = open('27-B.txt')
# N = A.readline()
# summ = 0
# ch = 0
# nech = 0
# minRaz1 = 10**9
# minRaz2 = 10**9
# minRaz3 = 10**9
# minRaz4 = 10**9
# for line in A:
#   x, y = map(int, line.split())
#   if x < y:
#     summ += x
#     if x % 2 == 0:
#       ch += 1
#     else:
#       nech += 1
#     if abs(x-y) % 2 != 0:
#       if abs(x-y) < minRaz1 and x % 2 == 0:
#         minRaz2 = minRaz1
#         minRaz1 = abs(x-y)
#       elif abs(x-y) < minRaz2 and x % 2 == 0:
#         minRaz2 = abs(x-y)
#       if abs(x-y) < minRaz3 and x % 2 != 0:
#         minRaz4 = minRaz3
#         minRaz3 = abs(x-y)
#       elif abs(x-y) < minRaz4 and x % 2 != 0:
#         minRaz4 = abs(x-y)
#   else:
#     summ += y
#     if y % 2 == 0:
#       ch += 1
#     else:
#       nech += 1
#     if abs(x-y) % 2 != 0:
#       if abs(x-y) < minRaz1 and y % 2 == 0:
#         minRaz2 = minRaz1
#         minRaz1 = abs(x-y)
#       elif abs(x-y) < minRaz2 and y % 2 == 0:
#         minRaz2 = abs(x-y)
#       if abs(x-y) < minRaz3 and yн % 2 != 0:
#         minRaz4 = minRaz3
#         minRaz3 = abs(x-y)
#       elif abs(x-y) < minRaz4 and y % 2 != 0:
#         minRaz4 = abs(x-y)

# if ch > nech:
#   if summ % 2 == 0:
#     print(summ)
#   elif minRaz3 <= minRaz1:
#     print(summ + minRaz3)
#   elif ch - nech != 1:
#     print(summ + minRaz1)
#   elif minRaz1 + minRaz2 < minRaz3:
#     print(summ + minRaz1 + minRaz2)
#   else:
#     print(summ + minRaz3)
# else:
#   pass

# f = open('26.txt')
# N = int(f.readline())
# box = [int(i) for i in f]
# box.sort(reverse  = True)
# ans = [box[0]]
# for i in range(1, N):
#     if ans[-1] - box[i] >= 3:
#         ans.append(box[i])
# print(len(ans), ans[-1])

# import string
# f = open('24 (29).txt')
# mx = 10 ** 9
# ans = ''
# for line in f:
#   if line.count('N') < mx:
#     mx = line.count('N')
#     ans = line
# d = dict().fromkeys(string.ascii_uppercase, 0)
# mn = 0
# result = ''
# for letter in d.keys():
#   d[letter] = ans.count(letter)
#   if d[letter] >= mn:
#     mn = d[letter]
#     result = letter
# print(result)
# f.close()

# f = open(r'17 (23).txt')
# data = [int(line) for line in f]
# c = 0
# maxNum = 0
# for i in range(len(data) - 1):
#   if (data[i] * data[i+1]) % 15 == 0 and (data[i] + data[i+1]) % 7 == 0:
#     c += 1
#     maxNum = max(data[i] + data[i+1], maxNum)

# print(c, maxNum)
# f.close()

# a = int(input())
# b = int(input())
# n = int(input())
# m = int(input())
# min1 = n + (n-1)*a
# min2 = m + (m-1)*b
# minT = max(min1, min2)
# max1 = n + (n+1)*a
# max2 = m + (m+1)*b
# maxT = min(max1, max2)
# if maxT >= minT:
#   print(minT, maxT)
# else:
#   print(-1)

# n = int(input())
# arr = []
# newG = 0
# for i in range(n):
#     a = int(input())
#     arr.append(a)
# for i in range(n-1, 0, -1):
#     if max(arr) <= n:
#         t = max(arr)
#         break
#     newG += arr[i] - n
#     arr[i] -= arr[i] - n
# print(t)

# t = int(input())
# maxA = 0
# ans = 0
# for i in range(t):
#     n, x = map(int, input().split())
#     a = list(map(int, input().split()))
#     maxA = max(a[0], 2*(x - a[n-1]))
#     for i in range(1, n):
#       maxA = max(maxA, a[i] - a[i-1])
#     print(maxA)

# t = int(input())
# for i in range(t):
#     s = input()
#     n = len(s)
#     ans = ''
#     arr = ''
#     if s[0] == ')':
#         ans = 'YES'
#         arr = '()' * n
#     elif s.count('(') == s.count(')') and s[-1] != '(':
#         ans = 'NO'
#     else:
#         ans = 'YES'
#         arr = '()' * n
#     if ans == 'NO':
#         print(ans)
#     else:
#         print(ans)
#         print(arr)

# t = int(input())
# for i in range(t):
#   n = int(input())
#   a = list(map(int, input().split()))
#   b = []
#   if a[0] == 1:
#     b.append(2)
#   else:
#     b.append(1)
#   for j in range(1, n):
#     if a[j] == b[j-1] + 1:
#       b.append(b[j-1] + 2)
#     else:
#       b.append(b[j-1] + 1)
#   print(b[n-1])

# t = int(input())
# ans = list()
# for i in range(t):
#   n = int(input())
#   arr = list(map(int, input().split()))
#   for j in range(n):
#     if j == n - 1:
#       ans.append(arr[j] + 1)
#     elif arr[j] < arr[j+1]:
#       ans.append(arr[j] + 1)
#     else:
#       ans.append(ans[j-1] + 1)
#   print(ans[-1])

# n = int(input())
# visited = [False] * (n + 1)
# prev = [None] * (n + 1)
# def dfs(start, visited, prev, g):
#     visited[start] = True
#     for u in g[start]:
#         if not visited[u]:
#             prev[u] = start
#             dfs(u,visited, prev, g)

# matrix = []
# for i in range(n):
#   line = list(map(int, input().split()))
#   matrix.append(line)
# r = 0
# g = [list() for i in range(n)]
# for i in range(n):
#   for j in range(i+1, n):
#     if matrix[i][j] == 1:
#       r += 1
#       g[i].append(j)
#       g[j].append(i)

# c = 0
# for i in range(n):
#   if not visited[i]:
#     c += 1
#     dfs(i, visited, prev, g)
# if c == 1 and r = n - 1:
#   print('YES')
# else:
#   print('NO')

# a = input()
# b = input()
# ans = 0
# s = set()

# for i in range(len(b)-1):
#   s.add(b[i:i+2])
# for i in range(len(a)-1):
#   if a[i:i+2] in s:
#     ans += 1
# print(ans)

# from math import gcd
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# ans = 0
# while a*d < b*c:
#   a += 1
#   b += 1
#   a //= gcd(a, b)
#   b //= gcd(a, b)
#   ans += 1
# if a == c and b == d:
#   print(ans)
# else:
#   print(0)

# a/b < c/d
# a*d < b*c

# dfs - обход в глубину

# visited = [False] * (n + 1)
# prev = [None] * (n + 1) #prev[5] = 3
# def dfs(start, visited, prev, g):
#     visited[start] = True
#     for u in g[start]:
#         if not visited[u]:
#             prev[u] = start
#             dfs(u)
# # start = 1 #зависит от задачи
# dfs(start, visited, prev, g)

# n, m = map(int, input().split())
# W = [list() for i in range(n + 1)]
# for i in range(m):
#     u, v = map(int, input().split())
#     W[u].append(v)
#     W[v].append(u)
# for row in W:
#   print(row)

# https://vos.olimpiada.ru/upload/files/Arhive_tasks/2021-22/mun/iikt/tasks-iikt-9-11-mun-msk-21-22.pdf
# n = int(input())
# a = int(input())
# b = int(input())
# total = a + 3 * b
# res = total // n
# if n % 3 != 0:
#   res = min(res, a // (n % 3))
# print(res)

# a = int(input())
# b = int(input())
# # a -= b
# # c = 0
# # day = 1
# # while b <= a:
# #   b += 1
# #   c += a - b
# #   day += 1
# # print(day)
# ans = 2*(a-b) + 1 + 1
# print(max(1, ans))

# from collections import deque

# d = deque()
# d.append(8)
# d.appendleft(7)
# d.pop()
# d.popleft()
# len(d)

# n = int(input())
# queue1 = deque()
# queue2= deque()
# res = ''

# for i in range(n):
#   gob = input().split()
#   if gob[0] == '+':
#     queue1.appendleft(gob[-1])
#     queue2.appendleft(queue1.pop())
#   elif gob[0] == '-':
#     res += queue2.pop()
#   elif gob[0] == '*':
#     if len(queue1) > len(queue2):
#       queue2.appendleft(queue1.pop())
#       queue2.appendleft(gob[-1])
#     elif len(queue1) < len(queue2):
#       queue1.append(queue2[0])
#       queue2.popleft()
#       queue2.appendleft(gob[-1])
#     elif len(queue1) == len(queue2):
#       queue2.appendleft(gob[-1])

# for i in res:
#   print(i)

# n = int(input())
# m = int(input())
# t = int(input())

# f = 4 * (n+m)**2 - 16 * t
# res = int((-2 * (n+m) + f**0.5) // -8)
# print(res)

# t1 = int(input())
# t2 = int(input())
# n1 = int(input())
# n2 = int(input())

# min1 = (n1 - 1) * t1 + n1
# max1 = (n1 + 1) * t1 + n1
# min2 = (n2 - 1) * t2 + n2
# max2 = (n2 + 1) * t2 + n2
# if max(min1, min2) < min(max1, max2):
#     print(max(min1, min2), min(max1, max2), sep=' ')
# else:
#   print(-1)

# way = input()
# horiz = 0
# vert = 0
# number = 0
# for i in range(len(way)):
#   if way[i] == 'N':
#     vert = vert + number
#     number = 0
#   elif way[i] == 'S':
#     vert = vert - number
#     number = 0
#   elif way[i] == 'W':
#     horiz = horiz - number
#     number = 0
#   elif way[i] == 'E':
#     horiz += number
#     number = 0
#   else:
#     number = number * 10 + int(way[i])
# if vert > 0:
#   print(vert, 'N', sep = '', end = '')
# else:
#   print(abs(vert), 'S', sep = '', end = '')
# if horiz > 0:
#   print(horiz, 'E', sep = '', end = '')
# else:
#   print(abs(horiz), 'W', sep = '', end = '')

# n = int(input())
# if n % 4 == 1 or n % 4 == 2:
#  print("IMPOSSIBLE")
# elif n % 4 == 3:
#  print("++-" + "+--+" * (n // 4))
# else:
#  print("+--+" * (n // 4))

# m = int(input())
# ans = 1
# t = 2
# while t*t <= m:
#   if m % (t*t) == 0:
#     ans = t*t
#   t += 1
# print(ans)

# p1 = list(map(int, input().split()))
# p2 = list(map(int, input().split()))
# s = 0
# go = True

# while go and len(p1) > 0 and len(p2) > 0:
#     s += 1
#     a = p1.pop(0)
#     b = p2.pop(0)
#     if a > b and (a != 0 and b != 9) or (a != 9 and b != 0):
#         p1.append(a)
#         p1.append(b)
#     else:
#         p2.append(b)
#         p2.append(a)
#     if s == 10 ** 6:
#         print('botva')
#         go = False
# if len(p1) == 0:
#     print('second', s)
# elif len(p2) == 0:
#     print('first', s)

# queue = []
# s = 0
# go = True

# def push(elem):
#     queue.append(elem)

# def front():
#     global s
#     if size() > 0:
#         return queue[s]
#     else:
#         return 'error'

# def size():
#     global s
#     return len(queue) - s

# def pop():
#     global s
#     if size() > 0:
#         s += 1
#         return queue[s-1]
#     else:
#         return 'error'

# stack = []
# count = int(input())
# way1 = list(map(int, input().split()))
# way2 = []
# res = 'YES'
# def push(elem):
#     stack.append(elem)
# def size():
#     return len(stack)
# def pop():
#     if size() > 0:
#         return stack.pop()
#     else:
#         return 'error'
# def back():
#     if size() > 0:
#         return stack[-1]
#     return -1
#     # else:
#     #     return 'error'
# for i in way1:
#   if size() == 0:
#     push(i)
#   elif back() > i:
#     push(i)
#   elif back() < i:
#     while size() > 0 and back() < i:
#       way2.append(pop())

# while size() > 0:
#   way2.append(pop())
# if way2 != sorted(way1):
#     res = 'NO'
# print(res)

# stack = []
# arr = input().split()

# def push(elem):
#     stack.append(elem)
# def size():
#     return len(stack)
# def pop():
#     if size() > 0:
#         return stack.pop()
#     else:
#         return 'error'
# def back():
#     if size() > 0:
#         return stack[-1]
#     else:
#         return 'error'
# def isint(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False

# for i in arr:
#     if isint(i):
#         push(int(i))
#     elif i == '+':
#         summ = int(pop()) + int(pop())
#         push(summ)
#     elif i == '-':
#         tmp1 = int(pop())
#         tmp2 = int(pop())
#         diff = tmp2 - tmp1
#         push(diff)
#     elif i == '*':
#         multi = int(pop()) * int(pop())
#         push(multi)

# print(back())

# stack = []
# go = True

# def push(elem):
#     stack.append(elem)

# def back():
#     if size() > 0:
#         return stack[-1]
#     else:
#         return 'error'

# def size():
#     return len(stack)

# def pop():
#     if size() > 0:
#         return stack.pop()
#     else:
#         return 'error'

# s = input()
# if len(s) == 0:
#     go = False
# for skb in s:
#     if skb == '(' or skb == '{' or skb == '[':
#         push(skb)
#     else:
#         if size() == 0:
#             # print('Мы зашли сюда')
#             go = False
#             break
#         if skb == ')' and back() != '(':
#             go = False
#             break
#         if skb == '}' and back() != '{':
#             go = False
#             break
#         if skb == ']' and back() != '[':
#             go = False
#             break
#         if skb == ')' and back() == '(':
#             pop()
#         if skb == '}' and back() == '{':
#             pop()
#         if skb == ']' and back() == '[':
#             pop()
# # print(go, size())
# if go and size() == 0:
#     print('yes')
# else:
#     print('no')

# stack = []
# go = True

# def push(elem):
#   stack.append(elem)
#   print('ok') #в дальнейшем не нужно

# def back():
#   if size() > 0:
#     return stack[-1]
#   else:
#     return 'error' #в дальнейшем не нужно

# def size():  #размер стека
#   return len(stack)

# def pop():
#   if size() > 0:
#     return stack.pop()
#   else:
#     return 'error' #в дальнейшем не нужно

# def clear(): #не всегда нужно
#   stack.clear()
#   print('ok') #в дальнейшем не нужно

# def exit(): #в дальнейшем не нужно
#   global go
#   go = False
#   print('bye') #в дальнейшем не нужно

# while go:
#   cmd = input().split()
#   if cmd[0] == 'push':
#     push(cmd[1])
#   if cmd[0] == 'pop':
#     print(pop())
#   if cmd[0] == 'back':
#     print(back())
#   if cmd[0] == 'size':
#     print(size())
#   if cmd[0] == 'clear':
#     clear()
#   if cmd[0] == 'exit':
#     exit()

# def solution(a, b, d):
#     kiosk1 = 0
#     kiosk2 = d

#     if (b-a) % 2 == 0:
#         home = (a+b) // 2
#         distance1 = abs(home - kiosk1)
#         distance2 = abs(home - kiosk2)
#         if distance1 > distance2:
#             return home, distance2
#         else:
#             return home, distance1
#     else:
#         var1 = (a+b) // 2
#         var2 = round((a+b) / 2)
#         distance1 = min(abs(var1 - kiosk1), abs(var1 - kiosk2))
#         distance2 = min(abs(var2 - kiosk1), abs(var2 - kiosk2))
#         if distance1 > distance2:
#             return var2, distance2
#         else:
#             return var1, distance1

# a, b, d = map(int, input().split())
# print(*solution(a, b, d))

# k, p = map(int, input().split())
# if k > 4:
#   dp = [0 for i in range(k+1)]
# else:
#   dp = [0 for i in range(10)]
# dp[2] = 1
# dp[3] = 1
# dp[4] = 2
# for i in range(5, k+1):
#     dp[i] = (dp[i] + dp[i-1] % p) % p
#     if i % 2 == 0:
#         dp[i] = (dp[i] + dp[i // 2] % p) % p
# print(dp[k] % p)

# n = int(input())
# a = list(map(int, input().split()))
# dp = [0] * (n+1)
# dp[0] = 0
# dp[1] = 0
# if n == 1:
#   print(0)
# else:
#   dp[2] = abs(a[1] - a[0])
#   for i in range(3, n+1):
#     dp[i] = min(dp[i-1] + abs(a[i-1] - a[i-2]), dp[i-2] + 3*abs(a[i-1] - a[i-3]))
#   print(dp[n])

# n = int(input())
# a = [0] * n
# b = [0] * n
# c = [0] * n
# for i in range(0, n):
#     a[i], b[i], c[i] = list(map(int, input().split()))
# if n == 1:
#   print(a[0])
# else:
#   dp = [0] * (n+1)
#   dp[1] = a[0]
#   dp[2] = min(dp[1] + a[1], b[0])
#   for i in range(3, n + 1):
#     dp[i] = min(dp[i-1] + a[i-1], dp[i-2] + b[i-2], dp[i-3] + c[i-3])

#   print(dp[n])

# from math import inf
# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# dp = [[0, 0] for i in range(n + 1)]
# dp[1][0] = 0
# dp[1][1] = 10**12
# for i in range(2, n + 1):
#   dp[i][0] = dp[i - 1][1]
#   dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + a[i - 1] - a[i - 2]
# print(dp[n][1])

# n = int(input())
# dp = [[0, 0, 0] for i in range(n+1)]
# dp[0][0] = 1
# dp[1][0] = 1
# dp[1][1] = 1
# dp[1][2] = 0
# for i in range(2, n+1):
#   dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
#   dp[i][1] = dp[i-1][0]
#   dp[i][2] = dp[i-2][0]
# print(dp[n][0] + dp[n][1] + dp[n][2])

# n, k = map(int, input().split())
# dp = [[0,0] for i in range(n+1)]
# dp[1][0] = 1
# dp[1][1] = k-1
# for i in range(2, n+1):
#   dp[i][0] = dp[i - 1][1]
#   dp[i][1] = (dp[i-1][0] + dp[i-1][1]) * (k-1)
# print(dp[n][0] + dp[n][1])

# N = int(input())
# Tshirt = list(map(int, input().split()))
# M = int(input())
# Pants = list(map(int, input().split()))
# ishirt = 0
# ipants = 0
# i = 0
# j = 0
# while i < N-1 or j < M-1:
#     if Tshirt[i] < Pants[j] and i < N - 1 or j == M - 1:
#         i += 1
#     elif j < M - 1:
#         j += 1
#     # print('###########')
#     # print('Current index: ', i, j)
#     # print('Current data: ', Tshirt[i], Pants[j])
#     # print('Current difference: ', abs(Tshirt[i] - Pants[j]))
#     if abs(Tshirt[i] - Pants[j]) < abs(Tshirt[ishirt] - Pants[ipants]):
#         ishirt = i
#         ipants = j
#     # print('Current best: ', ishirt, ipants)
#     # print('###########')

# print(Tshirt[ishirt], Pants[ipants])

# Повтори 8 [Вперёд 6 Направо 120]
# from turtle import *

# scale = 20
# for i in range(8):
#   forward(6*scale)
#   right(120)

# penup()
# for x in range(-100, 200, scale):
#   for y in range(-100, 100, scale):
#     setposition(x, y)
#     dot(3, 'red')


# done()


