def ms(l):
    if len(l)<=1:
        return l
    m=len(l)//2
    left=ms(l[:m])
    right=ms(l[m:])
    ans=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            ans.append(left[i])
            i=i+1
        else:
            ans.append(right[j])
            j=j+1
        j=j
    while i<len(left):
        ans.append(left[i])
        i=i+1
    while j<len(right):
        ans.append(right[j])
        j=j+1
    return ans
n=int(input())
if 1<=n<=100000:
    l=[]
    a=input().split()
    valid=True
    for i in a:
        e=int(i)
        if -1000000000<=e<=1000000000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        l=ms(l)
        for i in l:
            print(i,end=" ")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")