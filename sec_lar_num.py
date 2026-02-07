def find_second_largest(nums):
    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None
    else:
        return second_largest



nums = list(map(int, input("Enter numbers separated by space: ").split()))

result = find_second_largest(nums)

if result is None:
    print("No second largest number (all numbers may be same or only one number).")
else:
    print("Second largest number is:", result)
