def disarium(n):
    m=n
    c=0
    s=0
    while m!=0:
        m=m//10
        c+=1
    m=n
    while c!=0:
        l=m%10
        s+=l**c
        m=m//10
        c-=1
    if s==n:
        return True
    else:
        return False

n=int(input())
if disarium(n):
    print(n,"is disarium number")
else:
    print(n,"is not disarium number")