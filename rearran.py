arr=[12,6,7,8,9,10]
n=len(arr)
arr.sort()
arr[n//2:]=reversed(arr[n//2:])
print(arr)