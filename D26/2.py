def solve(n,a,b,c):
    global moves
    if n==1:
        print("Move plate 1 from",a,"to",c)
        moves=moves+1
        return
    solve(n-1,a,c,b)
    print("Move plate",n,"from",a,"to",c)
    moves=moves+1
    solve(n-1,b,a,c)
n=int(input())
if 1<=n<=15:
    moves=0
    solve(n,"A","B","C")
    print("Total Moves =",moves)
else:
    print("Invalid Input")