def palindrome(n):
    m=n
    t=0
    while m!=0:
        l=m%10
        t=t*10+l
        m=m//10
    if t==n:
        return True
    else:
        return False
   

n=int(input())
if palindrome(n):
    print(n,"is a palindrome.")
else:
    print(n,"is not a palindrome.")