Sub=list(map(int,input().split()))
if min(Sub)<0 or  max(Sub)>100:
    print("invalid input")
else:
    s=sum(Sub)/5
    if s>89:
        print("Grade A")
    elif s>79:
        print("Grade B")
    elif s>69:
        print("Grade C")    
    elif s>59:
        print("Grade D")    
    elif s>49:
        print("Grade E")
    else:
        print("Grade F")