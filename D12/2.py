s=input()
if 1<=len(s)<=10000:
    valid=True
    for i in s:
        if i<'a' or i>'z':
            valid=False
    if valid==True:
        ans=""
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>len(ans):
                    ans=s[l:r+1]
                l=l-1
                r=r+1
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>len(ans):
                    ans=s[l:r+1]
                l=l-1
                r=r+1
        print(ans)
    else:
        print("only lowercase english letter allow")
else:
    print("Invalid Input")