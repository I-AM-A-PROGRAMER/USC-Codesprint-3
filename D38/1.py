def solve(i,s):
    if i==len(d):
        print(s,end=" ")
        return
    for j in m[d[i]]:
        solve(i+1,s+j)
d=input()
valid=True
for i in d:
    if i<'2' or i>'9':
        valid=False
if 1<=len(d)<=4 and valid==True:
    m={}
    m["2"]="abc"
    m["3"]="def"
    m["4"]="ghi"
    m["5"]="jkl"
    m["6"]="mno"
    m["7"]="pqrs"
    m["8"]="tuv"
    m["9"]="wxyz"
    solve(0,"")
else:
    print("Invalid Input")