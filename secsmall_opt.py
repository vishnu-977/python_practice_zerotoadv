arr=[64,3,56,36,45,46,4]
small=float('inf')
second_small=float('inf')
for i in arr:
    if i<small:
        second_small=small
        small=i
    elif i!=small and i<second_small:
        second_small=i

print(second_small)