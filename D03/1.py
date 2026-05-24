n = int(input())
if 1<=n<=100000:
    l=[]
    numbers=input().split()
    for i in numbers:
        e=int(i)
        if 1<=e<=1000:
            l.append(e)
        else:
            print("code between 1 and 1000 allow")
    valid=True
    for i in range(1,n):
        if l[i]==l[i-1]:
            print("INVALID",i)
            valid=False
            break
    if valid==True:
        print("VALID")
else:
    print("n between 1 and 10^5 allow")