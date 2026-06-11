s=input()
t=input()
if 1<=len(t)<=len(s)<=100000:
    need={}
    for i in t:
        if i in need:
            need[i]=need[i]+1
        else:
            need[i]=1
    have={}
    count=0
    req=len(need)
    left=0
    ans=""
    mini=1000000000
    for right in range(len(s)):
        ch=s[right]
        if ch in have:
            have[ch]=have[ch]+1
        else:
            have[ch]=1
        if ch in need and have[ch]==need[ch]:
            count=count+1
        while count==req:
            if right-left+1<mini:
                mini=right-left+1
                ans=s[left:right+1]
            ch=s[left]
            have[ch]=have[ch]-1
            if ch in need and have[ch]<need[ch]:
                count=count-1
            left=left+1
    if ans=="":
        print(-1)
    else:
        print(ans)
else:
    print("Invalid Input")