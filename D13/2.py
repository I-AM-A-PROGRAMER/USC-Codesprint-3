s=input()
if 1<=len(s)<=100000:
    l=s.split()
    for i in range(len(l)-1,-1,-1):
        print(l[i],end="")
        if i!=0:
            print(" ",end="")
else:
    print("Invalid Input")