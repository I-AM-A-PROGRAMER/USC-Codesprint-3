s1=input()
s2=input()
if 1<=len(s1)<=100000 and 1<=len(s2)<=100000:
    valid=True
    for i in s1:
        if i<'a' or i>'z':
            valid=False
    for i in s2:
        if i<'a' or i>'z':
            valid=False
    if valid==True:
        a=sorted(s1)
        b=sorted(s2)
        if a==b:
            print("YES")
        else:
            print("NO")
    else:
        print("only lowercase english letters allowed")
else:
    print("Invalid Input")