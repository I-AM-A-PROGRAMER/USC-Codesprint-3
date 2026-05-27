n=int(input())
if 1<=n<=100:
    l=[]
    valid=True
    for i in range(n):
        s=input()
        if 1<=len(s)<=100:
            ok=True
            for j in s:
                if j <'a' or j>'z':
                    ok=False
            if ok==True:
                l.append(s)
            else:
                valid=False
        else:
            valid=False
    p=input()
    if valid==True:
        ans=[]
        for i in l:
            if i.startswith(p):
                ans.append(i)
        ans.sort()
        for i in ans:
            print(i)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")