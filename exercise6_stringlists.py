a = str(input("Enter a palindrome: "))
b = a[::-1]

print(f"You entered: {a}")
print(f"The reverse is: {b}")

if a == b:
    print(f"{a} is a palindrome!")
else:
    print("Not a palindrome.")
