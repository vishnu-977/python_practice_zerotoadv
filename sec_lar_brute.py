class SecondLargestNumber:
    def sec_Largest(self,arr):
        arr.sort()
        n=len(arr)
        if n<2:
                return None
        return arr[n-2]

arr=list(map(int,input("enter the array:").split()))
obj=SecondLargestNumber()
print("second largest number:",obj.sec_Largest(arr))