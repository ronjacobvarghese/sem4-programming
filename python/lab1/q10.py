def palindrome(n):
    if n==n[::-1]:
        return True
    else:
        return False
   

n=input()
if palindrome(n):
    print(n,"is a palindrome.")
else:
    print(n,"is not a palindrome.")