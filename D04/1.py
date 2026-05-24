s=input()
if 1<=len(s)<=200:
    vc=0
    c=0
    w=0
    v="aeiouAEIOU"
    for i in s:
        if i.isalpha():
            if i in v:
                vc=vc+1
            else:
                c=c+1
    l=s.split()
    for i in l:
        w=w+1
    print("Total vowel :",vc)
    print("Total consonants :",c)
    print("Total words :",w)
else:
    print("max length 200 chars")