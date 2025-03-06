import math

def mean(nums):
    return sum(nums) / (len(nums))

def std_deviation(nums, mean_value):
    variance = 0
    for n in nums:
        variance += (n - mean_value) ** 2
    variance_calc = variance / len(nums)
    return math.sqrt(variance_calc)

nums = []
while True:
    try:
        user_input = input("Please input a whole number: ")
        if user_input.lower() != "done":
            number = float(user_input)
            nums.append(number) 
        else:
            mean_value = mean(nums)
            print(f"Mean:", mean_value)
            print(f"Standard Deviation:", std_deviation(nums, mean_value))
            break
    except ValueError:
        print("Error: Please input a whole number.")
