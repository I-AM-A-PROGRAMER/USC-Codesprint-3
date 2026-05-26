n=int(input())
if 1<=n<=100:
    l=[]
    valid=True
    for i in range(n):
        s=input()
        if 1<=len(s)<=10000:
            l.append(s)
        else:
            valid=False
    if valid==True:
        ans=l[0]
        for i in l[1:]:
            while i.startswith(ans)==False:
                ans = ans[:-1]
        print(ans)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")