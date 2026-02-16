class MissingNumberXor:
    def find_missing(self,arr,n):
        xor_all=0
        xor_arr=0

        for i in range(1,n+1):
            xor_all^=i
        
        for i in arr:
            xor_arr^=i

        return xor_arr^xor_all
    
arr=list(map(int,input("enter the numbers:").split()))
n=int(input("enter the value of n:"))
obj=MissingNumberXor()
print("missing number:",obj.find_missing(arr,n))