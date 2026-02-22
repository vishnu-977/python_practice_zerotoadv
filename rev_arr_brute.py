arr=[1,3,4,5,6]
n=len(arr)
ans=[0]*n
for i in range(n):
    ans[i]=arr[n-1-i]
print(ans)