class SecondLargestNumber:
        def second_Large_Brute(self,arr):
                n=len(arr)
                if n<2:
                        return None
                largest=max(arr)
                second=float('-inf')

                for  i in arr:
                        if i!=largest and i>second:
                                second=i
                if second==float('-inf'):
                        return None
                
                return second
arr=list(map(int,input("enter the array :").split()))   
obj=SecondLargestNumber()
print("secondlargest:",obj.second_Large_Brute(arr))   