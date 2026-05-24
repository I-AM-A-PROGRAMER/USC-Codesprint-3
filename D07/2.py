s=input()
if 1<=len(s)<=100000:
    ans=""
    c=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            c=c+1
        else:
            ans=ans+s[i-1]+str(c)
            c=1
    ans=ans+s[len(s)-1]+str(c)
    print(ans)
else:
    print("Invalid Input")