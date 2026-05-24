n = int(input())
l=[]
zc = 0
for i in range(n):
    e=int(input())
    l.append(e)
    if e==0:
        zc+=1
ans = []
for x in l:
    if x != 0:
        ans.append(x)
for i in range(zc):
    ans.append(0)

for x in ans:
    print(x,end=" ")