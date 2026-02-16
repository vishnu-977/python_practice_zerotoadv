class MissingNumberBetter:
    def find_missing(self,arr,n):
        s=set(arr)
        for i in range(1,n+1):
            if i not in s:
                return i
arr=list(map(int,input("enter the numbers:").split()))
n=int(input("enter the value of n:"))
obj=MissingNumberBetter()
print("missing number:",obj.find_missing(arr,n))