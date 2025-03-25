"""
    Write a program to find the 20% of people with the largest age
    difference from other people in a large city.
"""
import time
import numpy as np
# Random age of 1.000.000 people
SIZE_PEOPLE = 10000
ages = np.random.randint(1, 100, size=SIZE_PEOPLE)

# Time start
start_time = time.time()

# Calculate age difference
age_diffs = dict()
for index in range(len(ages)):
    diffs = sum([abs(ages[index] - ages[jndex]) for jndex in range(len(ages)) if index != jndex])
    age_diffs[index] = diffs

# Sort age differences in descending order
sorted_age_diffs = sorted(age_diffs.items(), key=lambda item: item[1], reverse=True)
# Find 20% of people with the largest age difference
dct_return = dict(sorted_age_diffs[:int(0.2 * SIZE_PEOPLE)])

print(dct_return)
process_time = time.time() - start_time
print(process_time)
