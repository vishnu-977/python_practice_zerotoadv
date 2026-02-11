class PalindromeOptimal:
    def is_palindrome(self,s):
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

s=input("enter a string:")
obj=PalindromeOptimal()
print("is_palindrome:",obj.is_palindrome(s))


# tc = o(n) and sc=o(1)