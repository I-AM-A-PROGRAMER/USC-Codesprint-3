n=int(input())
if 0<=n<=100000:
    l=[]
    valid=True
    if n>0:
        a=input().split()
        for i in a:
            e=int(i)
            if -1000000000<=e<=1000000000:
                l.append(e)
            else:
                valid=False
    if valid==True:
        s=set(l)
        ans=0
        for i in s:
            if i-1 not in s:
                cur=i
                cnt=1
                while cur+1 in s:
                    cur=cur+1
                    cnt=cnt+1
                if cnt>ans:
                    ans=cnt
        print(ans)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")