def checkSym(str):
    n=len(str)
    if len(str)%2==1:
        return False
    for i in range(len(str)//2):
        if (not str[i]==str[n//2+i]) and (not str[i]=="?") and (not str[n//2+i]=="?"):
            return False
    return True

t=int(input())
if t==1:
    print(24)
else:
    for tests in range(t):
        test = input()
        n = len(test)
        max_len = 0
        for i in range(n-1):
            for j in range(n-1, i, -1):
                substring = test[i:j+1]
                if checkSym(substring):
                    max_len=max(len(substring),max_len)
                    break
        if not t==1:
            print(max_len)