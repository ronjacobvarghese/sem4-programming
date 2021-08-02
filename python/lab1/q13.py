def harm_sum(n):
    if n==1:
        return 1
    else:
        return (1/n)+harmonic_sum(n-1)

n=int(input())
print(harm_sum(n))