class Solution:
    def numberOfSubarrays(self,nums,k):
        n=len(nums)
        count=0
        
        for i in range(n):
            odd_count=0
            for j in range(i,n):
                if nums[j]%2==1:
                    odd_count+=1
                
                if odd_count==k:
                    count+=1
                elif odd_count>k:
                    break
        
        return count


nums=list(map(int,input("enter the numbers:").split()))
k=int(input("enter k:"))

sol=Solution()
result=sol.numberOfSubarrays(nums,k)
print("number of subarrays:",result)