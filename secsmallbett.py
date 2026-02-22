arr=[43,3,2,5,6,7,8,9]
mini=min(arr)
second=float('inf')
for i in arr:
    if i!=mini and i<second:
        second=i

print(second)