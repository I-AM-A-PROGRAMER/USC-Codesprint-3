a=input().split()
n=int(a[0])
x=int(a[1])
if 1<=n<=100 and 1<=x<=5000:
    cost=[]
    energy=[]
    valid=True
    for i in range(n):
        b=input().split()
        c=int(b[0])
        e=int(b[1])
        if 1<=c<=100 and 1<=e<=1000:
            cost.append(c)
            energy.append(e)
        else:
            valid=False
    if valid==True:
        dp=[0]*(x+1)
        for i in range(n):
            for j in range(cost[i],x+1):
                if dp[j-cost[i]]+energy[i]>dp[j]:
                    dp[j]=dp[j-cost[i]]+energy[i]
        print(dp[x])
    else:
        print("Invalid Input")
else:
    print("Invalid Input")