s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
res = ''
for char in alphabet:
    while char in s:
        res += char
        s = s.replace(char, chr(ord(char) + 1), 1)
if len(res) == 26:
    print(res)
else:
    print(-1)
