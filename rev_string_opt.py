class ReverseStringOptimal:
    def reverse(self,s):
        return s[::-1]
    
s=input("enter the string :")
obj=ReverseStringOptimal()
print("reversed_string:",obj.reverse(s))


# tc=o(n)
# sc=o(n)