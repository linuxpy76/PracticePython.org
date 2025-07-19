import random

list_length = 30
min_value = 1
max_value = 100

# Randomly generate lists
random1 = [random.randint(min_value, max_value) for _ in range(list_length)]
print(sorted(random1))
random2 = [random.randint(min_value, max_value) for _ in range(list_length)]
print(sorted(random2))

def remove_duplicates_set(values):
    return list(set(values))

def remove_duplicates_loop(values):
    list1 = []
    
    for i in values:
        if i not in list1:
            list1.append(i)
    
    list1.sort()
    return list1

print(remove_duplicates_set(random1))
print(remove_duplicates_loop(random2))