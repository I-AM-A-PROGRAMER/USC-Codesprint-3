s=input()
if 1<=len(s)<=100000:
    st=[]
    for i in range(len(s)-1,-1,-1):
        ch=s[i]
        if '0'<=ch<='9':
            st.append(int(ch))
        else:
            a=st.pop()
            b=st.pop()
            if ch=="+":
                st.append(a+b)
            elif ch=="-":
                st.append(a-b)
            elif ch=="*":
                st.append(a*b)
            else:
                st.append(int(a/b))
    print(st[0])
else:
    print("Invalid Input")