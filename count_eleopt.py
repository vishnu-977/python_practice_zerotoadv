from collections import defaultdict
arr=[4,3,2,4,5,6,4,7,4,7,8]
n=len(arr)
freq=defaultdict(int)

for i in range(n):
    freq[arr[i]]+=1

for key,value in freq.items():
    print(key,value)