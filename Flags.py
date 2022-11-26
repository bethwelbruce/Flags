'''def solution(A):
    if(len(A)<3):
        return 0
    P=[]
    for i in range(1,len(A)-1):
        if A[i]>A[i-1] and A[i]>A[i+1]:
            P.append(i)

    if len(P)==0:
        return 0
    elif len(P)==1:
        return 1
    c=1
    m=0

    for k in range(min(len(P))),int((len(A)**0.5)+1,0,-1):
        lastF=0
        c=1
        for i in range(1,len(P)):
            if P([i]-P[lastF])>= k and c<k:
                c+=1
                lastF=i
        if c<m:
            return m
        elif m<c:
        m=c
    return m
    pass
'''
 def solution(A):
    if(len(A)<3):
        return 0
    P=[]
    for i in range(1,len(A)-1):
        if A[i]>A[i-1] and A[i]>A[i+1]:
            P.append(i)

    if len(P)==0:
        return 0
    elif len(P)==1:
        return 1
    c=1
    m=0

    for k in range(1,len(P)):
        if (P[i]-P[lastF])>=k and c<k:
            c+=1
            lastF=i
        if c<m:
            return m
        elif m<c:
            m=c
    return m
    pass
