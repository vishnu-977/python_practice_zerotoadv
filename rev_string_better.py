class ReverseStringBetter:
    def reverse(self,s):
        rev=[]
        for i in s:
            rev.insert(0,i)
        return ''.join(rev)
    
s=input("enter a string:")
obj=ReverseStringBetter()
print("reversed_string:",obj.reverse(s))