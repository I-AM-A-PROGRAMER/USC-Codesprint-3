n=int(input())
if 1<=n<=100:
    l=[]
    valid=True
    for i in range(n):
        s=input()
        if 1<=len(s)<=100:
            ok=True
            for j in s:
                if j<'a' or j>'z':
                    ok=False
            if ok==True:
                l.append(s)
            else:
                valid=False
        else:
            valid=False
    if valid==True:
        for i in range(n):
            for j in range(n-1):
                v1=0
                v2=0
                for k in l[j]:
                    if k in "aeiou":
                        v1=v1+1
                for k in l[j+1]:
                    if k in "aeiou":
                        v2=v2+1
                if v1<v2 or (v1==v2 and len(l[j])>len(l[j+1])) or (v1==v2 and len(l[j])==len(l[j+1]) and l[j]>l[j+1]):
                    l[j],l[j+1]=l[j+1],l[j]
        for i in l:
            print(i)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")