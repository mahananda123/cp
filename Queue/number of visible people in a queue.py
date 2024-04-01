def canSeePersonsCount(heights):
    arr=[1]*len(heights)
    stk=[]
    n=len(heights)
    for i in range(n-1,-1,-1):
        c=0
        while stk and heights[stk[-1]]<heights[i]:
            stk.pop()
            c+=1
        if stk:
            arr[i]+=c
        else:
            arr[i]=c
        stk.append(i)
    return arr
arr=list(map(int,input().split()))
res=canSeePersonsCount(arr)
print(*res)
