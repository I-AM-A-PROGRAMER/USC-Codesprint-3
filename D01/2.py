n=int(input())
marks=[]
for i in range(n):
    e=int(input())
    if e<=100 and e>=0:
        marks.append(e)
    else:
        print("invalid marks")
        break
seen=[]
dupe="NO"
for m in marks:
    if m in seen:
        dupe="YES"
        break
    else:
        seen.append(m)
print(dupe)