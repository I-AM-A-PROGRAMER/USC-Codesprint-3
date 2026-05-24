n=int(input())
if 1<=n<=20:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        for j in range(2*(n-i)):
            print("@", end="")
        for j in range(i,0,-1):
            print(j, end="")
        print()
else:
    print("N between 1 nd 20 only")