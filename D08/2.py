n=int(input())
if 1<=n<=100000:
    l=[]
    a=input().split()
    for i in a:
        e=int(i)
        if 0<=e<=1000000000:
            l.append(e)
        else:
            print("Invalid Input")
    x=0
    for i in l:
        x=x^i
    if x==0:
        print("BALANCED")
    else:
        print("UNBALANCED")
else:
    print("Invalid Input")