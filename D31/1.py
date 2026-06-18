q=int(input())
if 1<=q<=100000:
    s1=[]
    s2=[]
    for i in range(q):
        a=input().split()
        if a[0]=="ADD":
            x=int(a[1])
            if 0<=x<=100000:
                s1.append(x)
        else:
            if len(s2)==0:
                while len(s1)>0:
                    s2.append(s1.pop())
            if len(s2)==0:
                print(-1)
            else:
                print(s2.pop())
else:
    print("Invalid Input")