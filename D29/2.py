s=input()
if 1<=len(s)<=100000:
    valid=True
    st=[]
    for i in s:
        if i<'a' or i>'z':
            valid=False
    if valid==True:
        for i in s:
            if len(st)>0 and st[-1]==i:
                st.pop()
            else:
                st.append(i)
        if len(st)==0:
            print("EMPTY")
        else:
            for i in st:
                print(i,end="")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")