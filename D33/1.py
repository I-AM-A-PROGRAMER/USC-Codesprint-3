n=int(input())
if 1<=n<=100000:
    l=[]
    valid=True
    for i in range(n):
        a=input().split()
        pid=int(a[0])
        p=int(a[1])
        if 1<=pid<=1000000000 and 1<=p<=1000000000:
            l.append([pid,p,i])
        else:
            valid=False
    if valid==True:
        l.sort(key=lambda x:(-x[1],x[2]))
        for i in l:
            print(i[0])
    else:
        print("Invalid Input")
else:
    print("Invalid Input")