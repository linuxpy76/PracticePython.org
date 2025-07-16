a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# New list with all element less than 5
# In one line


# Ask for input, output numbers in list less than that number
number = int(input("Enter a number: "))

x = [element for element in a if element < number]

print(x)



