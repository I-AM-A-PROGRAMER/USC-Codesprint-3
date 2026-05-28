n=int(input())
if 1<=n<=100:
    l=[]
    valid=True
    for i in range(n):
        a=input().split()
        name=a[0]
        score=int(a[1])
        if 0<=score<=1000000 and 1<=len(name)<=50:
            l.append([name,score])
        else:
            valid=False
    if valid==True:
        for i in range(n):
            for j in range(0,n-i-1):
                if l[j][1]>l[j+1][1]:
                    temp=l[j]
                    l[j]=l[j+1]
                    l[j+1]=temp
        for i in l:
            print(i[0],i[1])
    else:
        print("Invalid Input")
else:
    print("Invalid Input")