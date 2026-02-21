arr=[1,3,4,5,6,7,9]
n=len(arr)
maxi=arr[0]
for i in range(1,n):
    if arr[i]>maxi:
        maxi=arr[i]
print(maxi)