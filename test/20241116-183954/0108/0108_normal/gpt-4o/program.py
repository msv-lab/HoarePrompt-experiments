s = input()

# Target alphabet sequence
target = "abcdefghijklmnopqrstuvwxyz"
target_len = len(target)
i, j = 0, 0

# Iterate over the input string and try to match the target sequence
while i < len(s) and j < target_len:
    if s[i] == target[j]:
        j += 1
    i += 1

# If we have matched the entire target sequence, print the target
if j == target_len:
    print(target)
else:
    print(-1)
