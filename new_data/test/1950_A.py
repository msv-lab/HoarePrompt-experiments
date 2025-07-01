n = int(input())

for _ in range(n):
  arr = list(map(int, input().split()))

  if arr[0] > arr[1]:
    print('NONE')
  elif arr[1] > arr[2]:
    print('PEAK')
  elif arr[1] < arr[2]:
    print('STAIR')
  else:
    print('NONE')