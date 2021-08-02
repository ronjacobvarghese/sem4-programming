for _ in range(int(input())):
    n=int(input())
    if(n%2050):
        print(-1)
    else:
        print(sum([int(i) for i in str(n//2050)]))