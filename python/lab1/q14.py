def geo_sum(n):
    if n==0:
        return 1
    return 1/(3**n)+geometric_sum(n-1)

n=int(input())
print(geo_sum(n))