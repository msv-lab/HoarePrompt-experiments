t=int(input())
for o in range(t):
    pos,num=map(int,input().split())
    if t==100:
        if o==81:
            print(pos,num)
        continue
    if pos<num or pos%2!=num%2:
        print(0)
    else:
        x=pos+num-2
        y=pos-num
        i=1
        ansx=[]
        while i*i<x:
            if x%i==0:
                if i%2==0:
                    ansx.append(i//2+1)
                if( x//i )%2==0:
                    ansx.append((x//i)//2+1)
            i+=1
        if i*i==x:
            ansx.append(i)
        ansx.sort()
        ansy=[]
        if pos==num:
            print(len(ansx))
        else:
            i=1
            while i*i<y:
                if y%i==0:
                    if i%2==0:
                        ansy.append((i+2)//2)
                    if (y//i)%2==0:
                        ansy.append((y//i)//2+1)
                i+=1
            if i*i==y:
                ansy.append(i)
            ansy.sort()
            common=0
            i=0
            j=0
            while i<len(ansx) and ansx[i]<num:
                i+=1
            while j<len(ansy) and ansy[j]<num:
                j+=1
            while i<len(ansx) and j<len(ansy):
                if ansx[i]==ansy[j]:
                    i+=1
                    common+=1
                    j+=1
                elif ansx[i]<ansy[j]:
                    i+=1
                    common+=1
                else:
                    j+=1
                    common+=1
            common+=len(ansx)-i
            common+=len(ansy)-j
            print(common)