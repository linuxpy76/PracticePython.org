x = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# [EXPRESSION FOR_LOOPS CONDITIONALS]

c = [a for a in set(x) if a in y]

print(c)

