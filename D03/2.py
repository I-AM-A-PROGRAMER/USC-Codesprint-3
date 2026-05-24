n=int(input())
if 1<=n<=26:
    for i in range(n):
        for j in range(n):
            if j==i or j==n-i-1:
                ch=chr(65+i)
                print(ch,end=" ")
            else:
                print("*",end=" ")
        print()
else:
    print("enter n between 1 nd 26 only")