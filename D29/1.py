s=input()
if 1<=len(s)<=100000:
    st=[]
    num=0
    op="+"
    for i in range(len(s)):
        if s[i].isdigit():
            num=num*10+int(s[i])
        if not s[i].isdigit() or i==len(s)-1:
            if op=="+":
                st.append(num)
            elif op=="-":
                st.append(-num)
            elif op=="*":
                st.append(st.pop()*num)
            else:
                st.append(int(st.pop()/num))
            op=s[i]
            num=0
    ans=0
    for i in st:
        ans=ans+i
    print(ans)
else:
    print("Invalid Input")