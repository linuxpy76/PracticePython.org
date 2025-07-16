import random

# Randomly generate lists

list_length = 30
min_value = 1
max_value = 100

random1 = [random.randint(min_value, max_value) for _ in range(list_length)]
random2 = [random.randint(min_value, max_value) for _ in range(list_length)]

set1 = set(random1)
set2 = set(random2)

shared_set = set1 & set2

shared_list = list(shared_set)
shared_list.sort()

print(f"Random list 1: {random1}")
print(f"Random list 2: {random2}")
print(f"Shared elements: {shared_list}")
