s=input()
if 1<=len(s)<=100000:
    st=[]
    ans=""
    valid=True
    for i in s:
        if ('A'<=i<='Z') or ('a'<=i<='z'):
            ans=ans+i
        elif i=="(":
            st.append(i)
        elif i==")":
            while st[-1]!="(":
                ans=ans+st.pop()
            st.pop()
        else:
            while len(st)>0 and st[-1]!="(" and ((i=="+" or i=="-") or ((i=="*" or i=="/") and (st[-1]=="*" or st[-1]=="/"))):
                ans=ans+st.pop()
            st.append(i)
    while len(st)>0:
        ans=ans+st.pop()
    print(ans)
else:
    print("Invalid Input")