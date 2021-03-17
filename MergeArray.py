list1=[2,5,7,9]
list2=[1,3,6,8]

def merge(A, B, m, n):
    i=0
    j=0
    c=[]
    while (i<m and j<n):
        if A[i] <=B[j]:
            c.append(A[i])
            i +=1
        else:
            c.append([B[j]])
            j+=1
    for p in range (i,m):
        c.append(A[p])
    for q in range (j,n):
        c.append(B[q])

    print(c)

merge(list1,list2,len(list1),len(list2))

