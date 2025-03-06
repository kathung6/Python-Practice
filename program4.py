import random

total_rolls = 0

# returns rolling die value
def die_roll():
    return random.randint(1,6)

# dict to store the possbible sums of two dice
die_value_list = {}

for i in range(2, 13):
    die_value_list[i] = 0
    
# rolls 10000 times
while total_rolls < 10001:
    roll_1 = die_roll()
    roll_2 = die_roll()
    #adds the two rolls togethers
    total_of_rolls = roll_1 + roll_2
    # increases the count for this sum 
    die_value_list[total_of_rolls] += 1
    #increases total rolls
    total_rolls += 1
    
# prints each possible sum and how many times it occurred
for total, count in die_value_list.items():
    print(f"{total}: {count}")