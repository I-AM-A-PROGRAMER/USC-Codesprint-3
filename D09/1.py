n=int(input())
if 1<=n<=100000:
    l=[]
    a=input().split()
    for i in a:
        e=int(i)
        if -10000<=e<=10000:
            l.append(e*e)
        else:
            print("Invalid Input")
    l.sort()
    for i in l:
        print(i,end=" ")
else:
    print("Invalid Input")