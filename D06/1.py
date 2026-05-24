s=input()
if 1<=len(s)<=100:
    u=False
    l=False
    d=False
    for i in s:
        if i.isupper():
            u=True
        elif i.islower():
            l=True
        elif i.isdigit():
            d=True
    if u and l and d:
        print("STRONG")
    else:
        print("WEAK")
else:
    print("Invalid Input")