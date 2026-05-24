n=int(input())
if 1<=n<=50:
    l=[]
    for i in range(n):
        row=[]
        numbers=input().split()
        for j in numbers:
            e=int(j)
            if e==0 or e==1:
                row.append(e)
            else:
                print("Value only 0 or 1")
        l.append(row)
    for i in range(n):
        for j in range(n):
            if l[i][j]==1:
                print("O",end=" ")
            else:
                if (i>0 and l[i-1][j]==1) or (i<n-1 and l[i+1][j]==1) or (j>0 and l[i][j-1]==1) or (j<n-1 and l[i][j+1]==1):
                    print("X",end=" ")
                else:
                    print("S",end=" ")
        print()
else:
    print("n between 1 and 50")