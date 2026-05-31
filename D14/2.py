n=int(input())
if 1<=n<=100:
    l=[]
    valid=True
    a=input().split()
    for i in a:
        e=int(i)
        if 0<=e<=1000000000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        swaps=0
        for i in range(n-1):
            pos=i
            for j in range(i+1,n):
                if l[j]<l[pos]:
                    pos=j
            if pos!=i:
                l[i],l[pos]=l[pos],l[i]
                swaps=swaps+1
        for i in l:
            print(i,end=" ")
        print()
        print(swaps)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")