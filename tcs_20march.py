n=int(input())
arr=[]
for _ in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))

for i in range(n-1):
    mini=i
    for j in range(i+1,n):
        if arr[j][0]<arr[mini][0] or (arr[j][0]==arr[mini][0] and arr[j][1]<arr[mini][1]):
            mini=j
    arr[i],arr[mini]=arr[mini],arr[i]
for a,b in arr:
    print(a,b)