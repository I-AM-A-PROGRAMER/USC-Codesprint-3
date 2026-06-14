q=int(input())
if 1<=q<=100000:
    l=[]
    front=0
    for i in range(q):
        a=input().split()
        if a[0]=="REGISTER":
            l.append(int(a[1]))
        elif a[0]=="WITHDRAW":
            if front<len(l):
                front=front+1
            else:
                print(-1)
        else:
            if front<len(l):
                print(l[front])
                front=front+1
            else:
                print(-1)
else:
    print("Invalid Input")