class MissingNumberOptimal:
    def find_missing(self,arr,n):
        total_sum=n*(n+1)//2
        arr_sum=sum(arr)
        return total_sum-arr_sum
arr=list(map(int,input("enter the numbers:").split()))
n=int(input("enter the value of n:"))
obj=MissingNumberOptimal()
print("missing number:",obj.find_missing(arr,n))