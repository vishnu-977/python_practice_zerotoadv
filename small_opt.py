arr=[5,6,3,4,1,8]
n=len(arr)
min=arr[0]
for i in range(1,n):
    if arr[i]<min:
        min=arr[i]

print(min)