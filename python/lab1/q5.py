n=int(input());t=n
s=0
while t!=0:
    s+=(t%10)**3
    t=t//10
print("It is a Armstrong number" if s==n else "It is not an Armstrong number")