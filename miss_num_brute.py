class MissingNumberBrute:
    def find_missing(self,arr,n):
        for i in range(1,n+1):
            if i not in arr:
                return i

arr=list(map(int,input("enter the numbers:").split()))
n=int(input("enter the value of n:"))
obj=MissingNumberBrute()
print("missing number:",obj.find_missing(arr,n))