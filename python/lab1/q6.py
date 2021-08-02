n=int(input())
a=0
b=1
if n<=0:
    print("invalid number")
elif n==0:
    print(a)
else:
    for i in range(1,n+1):
        print(a)
        c=a+b
        a=b
        b=c