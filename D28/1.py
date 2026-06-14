s=input()
if 1<=len(s)<=100000:
    st=[]
    valid=True
    for i in s:
        if i=="(" or i=="[" or i=="{" or i=="<":
            st.append(i)
        else:
            if len(st)==0:
                valid=False
                break
            x=st.pop()
            if i==")" and x!="(":
                valid=False
                break
            if i=="]" and x!="[":
                valid=False
                break
            if i=="}" and x!="{":
                valid=False
                break
            if i==">" and x!="<":
                valid=False
                break
    if len(st)!=0:
        valid=False
    if valid==True:
        print("VALID")
    else:
        print("INVALID")
else:
    print("Invalid Input")