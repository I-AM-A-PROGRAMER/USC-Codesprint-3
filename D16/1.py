j=input()
s=input()
if 1<=len(j)<=50 and 1<=len(s)<=50:
    valid=True
    for i in j:
        if not((i>='a' and i<='z') or (i>='A' and i<='Z')):
            valid=False
    for i in s:
        if not((i>='a' and i<='z') or (i>='A' and i<='Z')):
            valid=False
    if valid==True:
        c=0
        for i in s:
            if i in j:
                c=c+1
        print(c)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")