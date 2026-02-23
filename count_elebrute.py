arr=[5,6,5,4,6,7,8,9,9,5]
n=len(arr)
visited=[False]*n
for i in range(n):
    if visited[i]:
        continue

    count=1
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            visited[j]=True
            count+=1
    print(arr[i],count)
