number = int(input("Enter a number: "))

if number % 4 == 0:
    print("FOUR")
elif number % 2 == 0:
    print("Even")
elif number % 2 != 0:
    print("Odd")
else:
    print("ERROR")

num = int(input("Enter a number: "))
check = int(input("Enter a number to divide by: "))

if num % check == 0:
    print(str(num) + " is divisible by " + str(check))
else:
    print(str(num) + " is NOT divisible by " + str(check))