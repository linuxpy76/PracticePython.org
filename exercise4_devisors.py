# Ask user for number and print list of all divisors of that number
x = int(input("Enter a number: "))

r = range(2, 101)

for elem in r:
    if x % elem == 0:
        print(elem)
    else:
        pass

