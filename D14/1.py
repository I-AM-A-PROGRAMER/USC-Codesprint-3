n=int(input())
if 2<=n<=100:
    l=[]
    valid=True
    a=input().split()
    for i in a:
        e=int(i)
        if 1<=e<=10000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                score=min(l[i],l[j])*(j-i)
                if score>ans:
                    ans=score
        print(ans)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")