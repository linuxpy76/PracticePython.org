import random

# Randomly generate lists

list_length = 30
min_value = 1
max_value = 100

random1 = [random.randint(min_value, max_value) for _ in range(list_length)]
print(sorted(random1))
# random2 = [random.randint(min_value, max_value) for _ in range(list_length)]

def remove_duplicates(v):

    set1 = set(v)
    v = list(set1)
    v.sort()
    return(v)

print(remove_duplicates(random1))