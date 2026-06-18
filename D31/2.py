q=int(input())
if 1<=q<=100000:
    st=[]
    mn=[]
    for i in range(q):
        a=input().split()
        if a[0]=="PUSH":
            x=int(a[1])
            if 0<=x<=1000000000:
                st.append(x)
                if len(mn)==0 or x<=mn[-1]:
                    mn.append(x)
        elif a[0]=="POP":
            if len(st)>0:
                x=st.pop()
                if x==mn[-1]:
                    mn.pop()
        else:
            if len(mn)==0:
                print(-1)
            else:
                print(mn[-1])
else:
    print("Invalid Input")