class PalindromeBrute:
    def is_Palindrome(self,s):
        rev=""
        for  i in s:
            rev=i+rev
        return s==rev

s=input("enter a string:")
obj=PalindromeBrute()
print("is_palindrome?",obj.is_Palindrome(s))


# t.c=o(n2)
# s.c=o(n)