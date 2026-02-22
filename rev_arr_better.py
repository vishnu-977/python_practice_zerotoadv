arr=[5,3,6,35,8,9]
n=len(arr)
p1=0
p2=n-1
while p1<p2:
    arr[p1],arr[p2]=arr[p2],arr[p1]
    p1+=1
    p2-=1

print(arr)