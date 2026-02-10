def reverse_string_brute(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
s=input("enter a string:")
print("reversed_string:",reverse_string_brute(s))