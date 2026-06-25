def solve(r):
    global found
    if r==n:
        found=True
        for i in range(n):
            s=""
            for j in range(n):
                if b[i]==j:
                    s=s+"Q"
                else:
                    s=s+"."
            print(s)
        return
    for c in range(n):
        ok=True
        for i in range(r):
            if b[i]==c or abs(b[i]-c)==abs(i-r):
                ok=False
                break
        if ok==True:
            b[r]=c
            solve(r+1)
n=int(input())
if 1<=n<=9:
    b=[-1]*n
    found=False
    solve(0)
    if found==False:
        print(-1)
else:
    print("Invalid Input")