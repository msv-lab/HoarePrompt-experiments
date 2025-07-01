import math
t = int(input())
for i in range (0, t):
  listvar = input().split()
  m = int(listvar[1])
  list = input().split()
  nums = []
  for k in list:
    nums.append(int(k))
  logs = []
  for k in nums:
    logs.append(int(math.log(k, 10) + 1))
  sl = sum(logs)
  for i in range (0, len(nums)):
    while (nums[i] % 10 == 0):
      nums[i] = int(nums[i] / 10)
    nums[i] = logs[i] - (math.floor(math.log(nums[i], 10)) + 1)
  nums.sort(reverse = True)
  sumdel = 0
  for i in range (0, len(nums)):
    if i % 2 == 0:
      sumdel += nums[i]
  if sl - sumdel > m: print("Sasha")
  else: print("Anna")