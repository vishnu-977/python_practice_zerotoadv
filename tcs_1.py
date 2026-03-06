n=int(input())
arr=list(map(int,input().split()))
target=int(input()) 

currSum=0
dici={}

for i in range(n):
    currSum+=arr[i]

    if currSum==target:
        print(*arr[:i+1])

        

    if (currSum-target) in dici:
        start=dici[currSum-target]+1
        print(*arr[start:i+1])

    dici[currSum]=i