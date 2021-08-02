for _ in range(int(input())):
    n,m=map(int,input().split())
    b=[sorted(map(int,input().split())) for i in range(n)]
    s=b[0]
    for i in range(1,n):
        a=m-1;j=0;d=b[i]
        while s[a]>d[j]:
            d[a],d[j]=d[j],d[a]
            s[a]=d[j]
            a-=1;j+=1
            
        
            
            
    